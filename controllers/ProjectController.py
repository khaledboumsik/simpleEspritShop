import sys
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
sys.path.append(r"C:\Users\Khaled\Desktop\ESPRITSHOP")
from flask import Flask, request, jsonify, Blueprint
from sqlalchemy import create_engine
from services.ProjectService import ProjectService

project_blue_print = Blueprint("project_blue_print", __name__)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/revamped_esprit_shop"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


@project_blue_print.route("/project/<id>", methods=["GET"])
def get_project_by_id(id):
    try:
        projectservice = ProjectService(engine)
        information = projectservice.get_project_by_ID(ID=id)
        if information:
            return jsonify(information), 200
        else:
            return jsonify({"message": "Project not found."}), 404
    except SQLAlchemyError as e:
        return jsonify({"message": "An error occurred while retrieving the project.", "error": str(e)}), 500
    except Exception as e:
        return jsonify({"message": "An unexpected error occurred.", "error": str(e)}), 500


@project_blue_print.route("/projects/<degree>", methods=["GET"])
def get_project_by_degree(degree):
    try:
        projectService = ProjectService(engine)
        information = projectService.get_projects_by_degree(Degree=degree)
        if information:
            return jsonify(information), 200
        else:
            return jsonify({"message": "No projects found with the specified degree."}), 404
    except SQLAlchemyError as e:
        return jsonify({"message": "An error occurred while retrieving the projects.", "error": str(e)}), 500
    except Exception as e:
        return jsonify({"message": "An unexpected error occurred.", "error": str(e)}), 500


@project_blue_print.route("/deleteProjectByID/<id>", methods=["DELETE"])
def delete_project_by_id(id):
    try:
        projectService = ProjectService(engine)
        success = projectService.delete_project_by_ID(id)
        
        if success:
            return jsonify({"message": "Project deleted successfully."}), 200
        else:
            return jsonify({"message": "Project not found."}), 404
    except IntegrityError as e:
        return jsonify({"message": "Data integrity error.", "error": str(e)}), 400
    except OperationalError as e:
        return jsonify({"message": "Database operational error.", "error": str
(e)}), 500
    except SQLAlchemyError as e:
        return jsonify({"message": "An error occurred while deleting the project.", "error": str(e)}), 500
    except Exception as e:
        return jsonify({"message": "An unexpected error occurred.", "error": str(e)}), 500


@project_blue_print.route("/project", methods=["POST"])
def create_project():
    try:
        # Validate input data
        data = request.json
        required_fields = ["About", "Degree", "Name", "Price", "Demo", "Picture"]
        for field in required_fields:
            if field not in data:
                return jsonify({"message": f"'{field}' is required."}), 400

        about = data["About"]
        degree = data["Degree"]
        name = data["Name"]
        price = data["Price"]
        demo = data["Demo"]
        picture = data["Picture"]

        project_service = ProjectService(engine)
        project_service.create_project(
            About=about, Degree=degree, Name=name, Price=price, Demo=demo, Picture=picture
        )
        return jsonify({"message": "Project created successfully"}), 201
    except IntegrityError as e:
        return jsonify({"message": "Data integrity error.", "error": str(e)}), 400
    except OperationalError as e:
        return jsonify({"message": "Database operational error.", "error": str(e)}), 500
    except SQLAlchemyError as e:
        return jsonify({"message": "An error occurred while creating the project.", "error": str(e)}), 500
    except Exception as e:
        return jsonify({"message": "An unexpected error occurred.", "error": str(e)}), 500

