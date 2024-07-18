from sqlalchemy import create_engine, ForeignKey, Boolean, String, Column, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from .ProjectRepository import Project
from main import db
from repository.ProjectRepository import Project


class Job(db.Model):
    __tablename__ = "job"

    Id = Column(Integer, primary_key=True, autoincrement=True)

    Email = Column(String(500))
    Phone = Column(Integer)
    ProjectId = Column(Integer, ForeignKey('project.Id'))  # ForeignKey referencing project.Id
    Information = Column(String(9000))

    # Define the relationship with Project
    project = relationship("Project", back_populates="jobs")
    def __init__(
        self,Email,Phone,ProjectId,Information
    
    ):
        self.Email = Email
        self.Phone = Phone
        self.Information = Information
        self.ProjectId=ProjectId

    def __repr__(self):
        return f"Email: {self.Email}\n Phone : {self.Phone}\n ProjectId: {self.ProjectId}\n Information: {self.Information}\nId: {self.Id}\n"
