from flask import Blueprint

user_bp=Blueprint("user_bp",__name__,"/users")

@user_bp.get("/test")
def handle_blueprint_test():
    return "blueprint Working"