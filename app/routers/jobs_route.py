from fastapi import APIRouter, Depends , Request, HTTPException , status
from sqlalchemy.orm import Session
from app.database.database import SessionLocal, get_db
from app.schemas.jobs_schema import JobCreate
from app.crud.jobs import create_job, fetch_jobs


router = APIRouter()

@router.post("/createjobs", status_code=status.HTTP_200_OK)
def create_job_route(job: JobCreate, db: Session = Depends(get_db)):
    try:
        print("Route /createjobs called")
        created_job = create_job(db=db, job=job)  # Call the CRUD function
        return {"message": "Job created successfully", "job": created_job}
    except Exception as e:
        print(f"Error while creating job: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the job."
        )

@router.get("/jobslist")
def get_all_jobs(db: Session = Depends(get_db)):
    job_list = fetch_jobs(db=db)
    return job_list