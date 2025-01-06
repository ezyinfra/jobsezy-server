from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    company_name: str
    job_role: str
    experience: str
    job_description: Optional[str] = None
    career_page_url: Optional[str] = None

    class Config:
        orm_mode = True
    

class JobResponse(JobCreate):
    id: int