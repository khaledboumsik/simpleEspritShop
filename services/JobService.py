from sqlalchemy.orm import sessionmaker
import sys

from repository.JobRepository import Job


class JobService:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)

    def create_job(
        self,Email,Phone,ProjectId,Information
    ):

        session = self.Session()
        job = Job(
            Email=Email,
            Phone=Phone,
            ProjectId=ProjectId,
            Information=Information,
        )
        print(job)
        session.add(job)
        session.commit()
        session.close()

    def get_job_by_ID(self, ID):
        session = self.Session()
        selected_job = session.query(Job).filter_by(Id=ID).first()
        session.close()
        return (
            {
                "Id": selected_job.Id,
                "Email": selected_job.Email,
                "Phone": selected_job.Phone,
                "ProjectId": selected_job.ProjectId,
                "Information": selected_job.Information,
            }
            if selected_job
            else {}
        )


    def get_all_jobs(self):
        session=self.Session()
        selected_jobs=(session.query(Job).all())
        session.close()
        return (
            [
                {
                    "Id": job.Id,
                    "Email": job.Email,
                    "Phone": job.Phone,
                    "ProjectId": job.ProjectId,
                    "Information": job.Information,
                }
                for job in selected_jobs
            ]
            if selected_jobs
            else {}
        )
    def delete_job_by_ID(self, Id):
        session = self.Session()
        try:
            job = session.query(Job).get(Id)
            if job:
                session.delete(job)
                session.commit()
                return True
            else:
                return False
        except:
            session.rollback()
            raise
        finally:
            session.close()
    def get_jobs_by_projectId(self, ProjectId):
        session = self.Session()
        selected_jobs = (
            session.query(Job).filter_by(ProjectId=ProjectId).all()
        )
        session.close()
        return (
            [
                {
                    "Id": job.Id,
                    "Email": job.Email,
                    "Phone": job.Phone,
                    "ProjectId": job.ProjectId,
                    "Information": job.Information,
                }
                for job in selected_jobs
            ]
            if selected_jobs
            else {}
        )
