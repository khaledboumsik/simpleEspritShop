from sqlalchemy.orm import sessionmaker
import sys,os
from repository.AdminRepository import Admin


class AdminService:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)

    def create_admin(self, Name, Password):
        session = self.Session()
        admin = Admin(
            Name=Name,
            Password=Password,

        )
        session.add(admin)
        session.commit()
        session.close()

    def get_admin_by_ID(self, ID):
        session = self.Session()
        selected_admin = session.query(Admin).filter_by(Id=ID).first()
        session.close()
        return (
            {
                "Id": selected_admin.Id,
                "Name": selected_admin.Name,
                "Password": selected_admin.Password,
            }
            if selected_admin
            else {}
        )
