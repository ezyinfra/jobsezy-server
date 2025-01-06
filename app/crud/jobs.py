from sqlalchemy.orm import Session
from app.models.jobs import Job
from app.schemas.jobs_schema import JobCreate

def create_job(db:Session, job: JobCreate):
    db_job = Job(
        company_name=job.company_name,
        job_role=job.job_role,
        experience=job.experience,
        job_description=job.job_description,
        career_page_url=job.career_page_url
    )
    db.add(db_job)
    db.commit
    db.refresh(db_job)
    print("data saved to db successfuly")
    return db_job
