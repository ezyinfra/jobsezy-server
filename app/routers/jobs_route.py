from fastapi import APIRouter, Depends , Request, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal, get_db
from app.schemas.jobs_schema import JobCreate
from app.crud.jobs import create_job


router = APIRouter()

@router.post("/createjobs")
def create_job_route(job: JobCreate , db : Session = Depends(get_db)):
    print("route createjobs available")
    create_job(db=db, job=job)
    return create_job
