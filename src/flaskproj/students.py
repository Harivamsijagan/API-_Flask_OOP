from flask import Flask, request, jsonify

app = Flask(__name__)

class Student:

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"

    def get_details(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
            "grade": self.calculate_grade()
        }

    def update_marks(self, marks):
        self.marks = marks


class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def update_student(self, student_id, data):
        student = self.find_student(student_id)

        if student is None:
            return None

        if "name" in data:
            student.name = data["name"]

        if "age" in data:
            student.age = data["age"]

        if "course" in data:
            student.course = data["course"]

        if "marks" in data:
            student.update_marks(data["marks"])

        return student

    def delete_student(self, student_id):
        student = self.find_student(student_id)

        if student is None:
            return False

        self.students.remove(student)
        return True

    def get_all_students(self):
        return self.students

    def get_passed_students(self):
        passed = []

        for student in self.students:
            if student.marks >= 40:
                passed.append(student)

        return passed

manager = StudentManager()

@app.post("/students")
def add_student():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}), 400

    required_fields = ["student_id", "name", "age", "course", "marks"]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"{field} is required"
            }), 400

    student = Student(
        data["student_id"],
        data["name"],
        data["age"],
        data["course"],
        data["marks"]
    )

    manager.add_student(student)

    return jsonify(student.get_details()), 201


@app.get("/students")
def get_students():

    students = manager.get_all_students()

    return jsonify([
        student.get_details()
        for student in students
    ]), 200

@app.get("/students/<int:student_id>")
def get_student(student_id):

    student = manager.find_student(student_id)

    if student is None:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify(student.get_details()), 200

@app.patch("/students/<int:student_id>")
def update_student(student_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Invalid input"
        }), 400

    student = manager.update_student(student_id, data)

    if student is None:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify(student.get_details()), 200

@app.delete("/students/<int:student_id>")
def delete_student(student_id):

    result = manager.delete_student(student_id)

    if not result:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify({
        "message": "Student deleted successfully"
    }), 200

@app.get("/students/passed")
def get_passed_students():

    students = manager.get_passed_students()

    return jsonify([
        student.get_details()
        for student in students
    ]), 200

@app.get("/students/stats")
def get_stats():

    students = manager.get_all_students()

    if len(students) == 0:
        return jsonify({
            "total_students": 0,
            "average_marks": 0,
            "highest_marks": 0,
            "lowest_marks": 0
        }), 200

    marks = [student.marks for student in students]

    return jsonify({
        "total_students": len(students),
        "average_marks": sum(marks) / len(marks),
        "highest_marks": max(marks),
        "lowest_marks": min(marks)
    }), 200

@app.get("/test")
def handle_test():
    return "Working"


if __name__ == "__main__":
    app.run(debug=True)

