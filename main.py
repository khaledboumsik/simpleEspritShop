from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost:3306/espritshopmaindb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Enable CORS for all origins on all routes
    CORS(app)

    with app.app_context():
        # Import your models and controllers here
        from repository.ProjectRepository import Project
        from repository.JobRepository import Job
        from repository.AdminRepository import Admin

        from controllers.ProjectController import project_blue_print
        from controllers.JobController import job_blue_print
        from controllers.AdminController import admin_blue_print

        app.register_blueprint(project_blue_print)
        app.register_blueprint(job_blue_print)
        app.register_blueprint(admin_blue_print)

    return app
