from sqlalchemy.orm import sessionmaker
import sys

from repository.ProjectRepository import Project


class ProjectService:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)

    def create_project(self, About, Degree, Name, Price, Demo,Picture):
        session = self.Session()
        project = Project(About=About, Degree=Degree, Name=Name, Price=Price, Demo=Demo,Picture=Picture)
        session.add(project)
        session.commit()
        session.close()
    def get_all_projects(self):
        session=self.Session()
        selected_projects=(session.query(Project).all())
        session.close()
        return (
            [
                {
                    "Id": project.Id,
                    "About": project.About,
                    "Degree": project.Degree,
                    "Name": project.Name,
                    "Price": project.Price,
                    "Demo": project.Demo,
                    "Picture": project.Picture,
                }
                for project in selected_projects
            ]
            if selected_projects
            else {}
        )
    def get_projects_by_degree(self, Degree):
        session = self.Session()
        selected_projects = session.query(Project).filter_by(Degree=Degree).all()
        session.close
        return (
            [
                {
                    "id": project.Id,
                    "About": project.About,
                    "Degree": project.Degree,
                    "Name": project.Name,
                    "Price": project.Price,
                    "Demo": project.Demo,
                    "Picture":project.Picture,
                }
                for project in selected_projects
            ]
            if selected_projects
            else {}
        )
    def delete_project_by_ID(self, id):
        session = self.Session()
        try:
            project = session.query(Project).get(id)
            if project:
                session.delete(project)
                session.commit()
                return True
            else:
                return False
        except:
            session.rollback()
            raise
        finally:
            session.close()
    def get_project_by_ID(self, ID):
        session = self.Session()
        selected_project = session.query(Project).filter_by(Id=ID).first()
        session.close()
        return (
            {
                "id": selected_project.Id,
                "About": selected_project.About,
                "Degree": selected_project.Degree,
                "Name": selected_project.Name,
                "Price": selected_project.Price,
                "Demo": selected_project.Demo,
                "Picture":selected_project.Picture,
            }
            if selected_project
            else {}
        )
