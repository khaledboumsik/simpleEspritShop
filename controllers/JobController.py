import sys
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
sys.path.append(r"C:\Users\Khaled\Desktop\ESPRITSHOP")
from flask import Flask, request, jsonify, Blueprint
from sqlalchemy import create_engine
from services.JobService import JobService

job_blue_print = Blueprint("job_blue_print", __name__)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/revamped_esprit_shop"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

@job_blue_print.route("/job/<id>", methods=["GET"])
def get_job_by_id(id):
    try:
        job_service = JobService(engine)
        information = job_service.get_job_by_ID(ID=id)
        if information:
            return jsonify(information), 200
        else:
            return jsonify({"message": "Job not found."}), 404
    except SQLAlchemyError as e:
        return jsonify({"message": "An error occurred while retrieving the job.", "error": str(e)}), 500
    except Exception as e:
        return jsonify({"message": "An unexpected error occurred.", "error": str(e)}), 500

@job_blue_print.route("/jobs", methods=["GET"])
def get_all_jobs():
    try:
        job_service = JobService(engine)
        information = job_service.get_all_jobs()
        return jsonify(information), 200
    except SQLAlchemyError as e:
        return jsonify({"message": "An error occurred while retrieving jobs.", "error": str(e)}), 500
    except Exception as e:
        return jsonify({"message": "An unexpected error occurred.", "error": str(e)}), 500

@job_blue_print.route("/job_by_project_id/<id>", methods=["GET"])
def get_jobs_by_projectId(id):
    try:
        job_service = JobService(engine)
        information = job_service.get_jobs_by_projectId(ProjectId=id)
        if information:
            return jsonify(information), 200
        else:
            return jsonify({"message": "No jobs found for the specified Project ID."}), 404
    except SQLAlchemyError as e:
        return jsonify({"message": "An error occurred while retrieving jobs by Project ID.", "error": str(e)}), 500
    except Exception as e:
        return jsonify({"message": "An unexpected error occurred.", "error": str(e)}), 500

@job_blue_print.route("/delete_job/<id>", methods=["DELETE"])
def delete_job_by_id(id):
    try:
        job_service = JobService(engine)
        success = job_service.delete_job_by_ID(id)
        
        if success:
            return jsonify({"message": "Job deleted successfully."}), 200
        else:
            return jsonify({"message": "Job not found."}), 404
    except IntegrityError as e:
        return jsonify({"message": "Data integrity error while deleting job.", "error": str(e)}), 400
    except OperationalError as e:
        return jsonify({"message": "Database operational error.", "error": str(e)}), 500
    except SQLAlchemyError as e:
        return jsonify({"message": "An error occurred while deleting the job.", "error": str(e)}), 500
    except Exception as e:
        return jsonify({"message": "An unexpected error occurred.", "error": str(e)}), 500

@job_blue_print.route("/job", methods=["POST"])
def create_job():
    try:
        data = request.json
        required_fields = ["Email", "Phone", "ProjectId", "Information"]
        for field in required_fields:
            if field not in data:
                return jsonify({"message": f"'{field}' is required."}), 400

        Email = data["Email"]
        Phone = data["Phone"]
        ProjectId = data["ProjectId"]
        Information = data["Information"]
        job_service = JobService(engine)
        job_service.create_job(
            Email=Email,
            Phone=Phone,
            ProjectId=ProjectId,
            Information=Information
        )
        return jsonify({"message": "Job created successfully"}), 201
   
    except IntegrityError as e:
        return jsonify({"message": "Data integrity error while creating job.", "error": str(e)}), 400
    except OperationalError as e:
        return jsonify({"message": "Database operational error.", "error": str(e)}), 500
    except SQLAlchemyError as e:
        return jsonify({"message": "An error occurred while creating the job.", "error": str(e)}), 500
    except Exception as e:
        return jsonify({"message": "An unexpected error occurred.", "error": str(e)}), 500
