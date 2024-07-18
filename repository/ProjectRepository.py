from sqlalchemy import create_engine, ForeignKey, String, Column, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from main import db


class Project(db.Model):
    __tablename__ = "project"
    
    Id = Column("Id",Integer, primary_key=True, autoincrement=True)
    About = Column("About",String)
    Degree = Column("Degree",Integer)
    Name = Column("Name",String)
    Price = Column("Price",Integer)
    Demo = Column("Demo",String)
    Picture = Column("Picture",String)

    # Define the relationship with Job
    jobs = relationship("Job", back_populates="project") 
    def __init__(self, About, Degree, Name, Price, Demo,Picture):
        self.About = About
        self.Degree = Degree
        self.Name = Name
        self.Price = Price
        self.Demo = Demo
        self.Picture=Picture

    def __repr__(self):
        return f"About: {self.About}\n ID: {self.Identifier}\n Degree: {self.Degree}\n Name: {self.Name}\n Price: {self.Price} \n  Demo: {self.Demo}"
