from sqlalchemy import create_engine, ForeignKey, Boolean, String, Column, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from main import db


class Admin(db.Model):
    __tablename__ = "admin"
    Id = Column("Id", Integer, primary_key=True, autoincrement=True)
    Name = Column("Name", String)
    Password = Column("Password", String)
    def __init__(self, Name, Password):
        self.Name = Name
        self.Password = Password

    def __repr__(self):
        return f"Login : {self.Login}\n ID: {self.Identifier}\n Password: {self.Password}\n Status: {self.Status}\n PhoneNumber: {self.PhoneNumber}\n Email: {self.Email}"
