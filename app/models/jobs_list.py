from sqlalchemy import Column, Integer, String
from app.database.database import Base  # Assuming you have a Base class in database.py
from app.models.mixins import Timestamp 

class JobList(Base , Timestamp):
    __tablename__ = 'jobs_list'  # The name of the table in the database

    job_id = Column(Integer, primary_key=True, autoincrement=True)  # Job ID as primary key
    company_name = Column(String, nullable=False)  # Company name (required)
    job_role = Column(String, nullable=False)  # Job role (required)
    job_description = Column(String, nullable=True)  # Job description (optional)
    career_page_url = Column(String, nullable=True)  # Career page URL (optional)
