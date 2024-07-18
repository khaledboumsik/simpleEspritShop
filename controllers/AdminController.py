import sys
import requests
from hasher import hash_password,verify_password
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from services.AdminService import AdminService
from flask import Blueprint

admin_blue_print = Blueprint("admin_blue_print", __name__)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/revamped_esprit_shop"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


@admin_blue_print.route("/admin/<id>", methods=["GET"])
def get_admin_by_id(id):
    adminService = AdminService(engine)
    information = adminService.get_admin_by_ID(ID=id)
    return jsonify(information)


@admin_blue_print.route("/admin", methods=["POST"])
def create_user():
    Name = request.json.get("Name")
    password = request.json.get("Password")

    admin_serivce = AdminService(engine)
    admin_serivce.create_admin(
        Name=Name,
        Password=password,
    )
    return jsonify({"message": "Admin created successfully"}), 201
@admin_blue_print.route("/verify", methods=["POST"])
def verify_admin():
    try:
        data = request.json
        Name = data.get("Name")
        Password = data.get("Password")

        if not Name or not Password:
            return jsonify({"message": "Name and Password are required."}), 400

        # Make a GET request to the /admin/0 endpoint
        response = requests.get("http://127.0.0.1:5000/admin/0")
        
        if response.status_code != 200:
            return jsonify({"message": "Failed to retrieve admin data."}), 500
        
        admin = response.json()
        print(admin.get("Password") ,Password)
        print(verify_password(admin.get("Password") ,Password), admin.get("Name") == Name)
        if admin.get("Name") == Name and verify_password(admin.get("Password") ,Password):
            return jsonify({"message": "Admin credentials verified successfully."}), 200
        else:
            return jsonify({"message": "Invalid credentials."}), 401

    except Exception as e:
        return jsonify({"message": "An error occurred while verifying admin credentials.", "error": str(e)}), 500