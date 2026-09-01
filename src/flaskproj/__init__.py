# from flask import Flask,request,jsonify
# import requests


# app = Flask(__name__)

# menu = [
#     {"name": "Margherita Pizza", "price": 299},
#     {"name": "Chicken Biryani", "price": 249},
#     {"name": "Paneer Butter Masala", "price": 199},
#     {"name": "Veg Burger", "price": 129},
#     {"name": "Masala Dosa", "price": 99},
#     {"name": "Cold Coffee", "price": 79}
# ]
# orders ={}

# @app.get("/menu")
# def get_the_food():
#     return menu

# @app.post("/orders")
# def place_order():
#    data = request.get_json()
#    for order in data:
#        order["status"] = "ongoing"
#        orders[order["orderID"]]= order

#        return jsonify(data),201
# @app.patch("/orders/<orderId>/complete")
# def complete_order(orderId):
#     if orderId not in orders:
#         return jsonify({"error": "Order not found"}), 404
    
#     orders[orderId]["status"] = "completed"

#     return jsonify(orders[orderId])
   
# @app.get("/orders/ongoing")
# def ongoing_orders():
#     return jsonify([
#         order for order in orders.values()
#         if order["status"] == "ongoing"
#     ])

# if __name__=="__main__":
#     app.run(debug=True)

    
    
        
# from flask import Flask
# # import requests
# import json
# import uuid
# app = Flask(__name__)

# @app.route("/menu",methods=["GET","POST"])
# def get_the_food():
  
#   with open("./data.json","r") as file:
#     data = json.load(file)
  
  
#     return data["menu"]

# @app.post("/menu/<nameoffood>/price/<int:quantity>/<status>")
# def place_order(nameoffood,quantity,status):
  
#   with open("./data.json","r") as file:
#     data = json.load(file)
#     price = 0
#     for item in data["menu"]:
#       if nameoffood.lower() == item["name"].lower():
#         price = item["price"]
#         break
#     if price == 0:
#       return "No Food Item"
    
#     new_order = {
      
#       "orderId" : str(uuid.uuid4()),
#       "orderStatus" : status,
#       "orderItems" : [
#         {
#          "name" : nameoffood,
#          "price" : price,
#          "quantity" : quantity

#          }
#       ]
#     }
#     data["orders"].append(new_order)
#     with open("./data.json","w") as file:
#         json.dump(data,file)
    
#     return new_order


# @app.patch("/menu/<orderID>/<status>")
# def status_place_order(orderID,status):
  
#   with open("./data.json","r") as file:
#     data = json.load(file)
#     for item in data["orders"]:
#       if item["orderId"] == orderID:
#         item["orderStatus"] = status

#     # data["orders"].append(new_order)
#         with open("./data.json","w") as file:
#             json.dump(data,file)
#         return item
#   return "Item not found"



# @app.delete("/menu/<orderStatus>")
# def remove_Completed_food_order(orderStatus):
#   with open("./data.json","r") as file:
#     data = json.load(file)
#   for item in data["orders"]:
#     if item["orderStatus"].lower() == orderStatus.lower():
#       data["orders"].remove(item)
#       with open("./data.json","w")  as file:
#         json.dump(data,file)
#       return "order deleted"
#   return "Order Not Found"

# if __name__ == "__main__":
#   app.run(debug=True)          
  

# from flask import Flask, render_template_string
# import requests

# app = Flask(__name__)
# API_KEY = "c3b743d3c36415b62a6b61c80e703c0a"

# html_template = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Weather for {{ location }}</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             max-width: 600px;
#             margin: 50px auto;
#             padding: 20px;
#             background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#             color: white;
#         }
#         .weather-card {
#             background: rgba(255, 255, 255, 0.2);
#             backdrop-filter: blur(10px);
#             border-radius: 15px;
#             padding: 30px;
#             box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
#         }
#         h1 {
#             text-align: center;
#             margin-bottom: 30px;
#         }
#         .temp {
#             font-size: 48px;
#             font-weight: bold;
#             text-align: center;
#             margin: 20px 0;
#         }
#         .details {
#             display: flex;
#             justify-content: space-around;
#             margin-top: 20px;
#         }
#         .detail-item {
#             text-align: center;
#         }
#         .label {
#             font-size: 14px;
#             opacity: 0.8;
#         }
#         .value {
#             font-size: 18px;
#             font-weight: bold;
#         }
#     </style>
# </head>
# <body>
#     <div class="weather-card">
#         <h1> Weather in {{ location }}</h1>
#         <div class="temp">{{ temp }}°C</div>
#         <div class="details">
#             <div class="detail-item">
#                 <div class="label">Latitude</div>
#                 <div class="value">{{ lat }}</div>
#             </div>
#             <div class="detail-item">
#                 <div class="label">Longitude</div>
#                 <div class="value">{{ lon }}</div>
#             </div>
#         </div>
#     </div>
# </body>
# </html>
# """

# @app.route("/weather/<lat>/<lon>")
# def weather_page(lat, lon):
#     try:
#         url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
#         response = requests.get(url)
#         data = response.json()
        
#         location = data.get("name", "Unknown")
#         temp = round(data["main"]["temp"], 2)
        
#         return render_template_string(html_template, location=location, temp=temp, lat=lat, lon=lon)
#     except Exception as e:
#         return f"<h1>Error: {str(e)}</h1>"

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)





# from flask import Flask, render_template
# import requests

# API_KEY = "c209b0ba0cbc0279a8fa500ca3830809"


# app = Flask(__name__)


# city = [
#     {"name": "Delhi", "lat": 28.6139, "lng": 77.2090},
#     {"name": "Mumbai", "lat": 19.0760, "lng": 72.8777},
#     {"name": "Bangalore", "lat": 12.9716, "lng": 77.5946},
#     {"name": "Hyderabad", "lat": 17.3850, "lng": 78.4867},
#     {"name": "Kolkata", "lat": 22.5726, "lng": 88.3639},
#     {"name": "Chennai", "lat": 13.0827, "lng": 80.2707},
#     {"name": "Pune", "lat": 18.5204, "lng": 73.8567},
#     {"name": "Ahmedabad", "lat": 23.0225, "lng": 72.5714},
#     {"name": "Jaipur", "lat": 26.9124, "lng": 75.7873},
#     {"name": "Lucknow", "lat": 26.8467, "lng": 80.9462},
#     {"name": "Chandigarh", "lat": 30.7333, "lng": 76.7794},
#     {"name": "Indore", "lat": 22.7196, "lng": 75.8577},
#     {"name": "Kochi", "lat": 9.9312, "lng": 76.2673},
#     {"name": "Visakhapatnam", "lat": 17.6869, "lng": 83.2185},
#     {"name": "Surat", "lat": 21.1458, "lng": 72.8336},
#     {"name": "Vadodara", "lat": 22.3072, "lng": 73.1812},
#     {"name": "Nagpur", "lat": 21.1458, "lng": 79.0882},
#     {"name": "Bhopal", "lat": 23.1815, "lng": 79.9864},
#     {"name": "Guwahati", "lat": 26.1445, "lng": 91.7362},
#     {"name": "Ranchi", "lat": 23.3441, "lng": 85.3096},
#     {"name": "Amritsar", "lat": 31.6340, "lng": 74.8711},
#     {"name": "Thrissur", "lat": 10.5276, "lng": 76.2144},
#     {"name": "Nashik", "lat": 19.9975, "lng": 73.7898},
#     {"name": "Aurangabad", "lat": 19.8762, "lng": 75.3433}
# ]



# @app.get("/")
# def handle_home():
#     return render_template('index.html', city_list=city)

# @app.get("/<lat>/<lng>")
# def handle_climate(lat, lng):
#     REQUEST_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={API_KEY}"
#     response = requests.get(REQUEST_URL)
#     data = response.json()
#     city_name = data['name']
#     temp = data['main']['temp'] - 273.15
#     weather_tag = ""
#     if temp > 30:
#         weather_tag = "SUPER HOT"
#     elif 25 < temp < 30:
#         weather_tag ="OKAYish"
#     elif 20 < temp < 25:
#         weather_tag = "Cool"
#     elif temp < 20:
#         weather_tag = "Shivering Cold"

#     return render_template(
#         "climate.html",
#         city_name=city_name,
#         temp=temp,
#         weather_tag=weather_tag
#     )


# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask , render_template

# app = Flask(__name__)
# @app.route("/home",methods=["GET"])

# def handle_home():
#   return render_template("index.html")

# @app.route("/aboutus")

# def aboutUs():
#   return render_template("index.html")

# if __name__ == "__main__":
#   app.run(debug=True)




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


if __name__ == "__main__":
    app.run(debug=True)

