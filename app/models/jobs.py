from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base
from app.models.mixins import Timestamp 


class Job(Base, Timestamp):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, autoincrement=True , index=True)
    company_name = Column(String(255), nullable=False)
    job_role = Column(String(255), nullable=False)
    experience = Column(String(255), nullable=False)
    job_description = Column(String(5000), nullable=True)
    career_page_url = Column(String(2083), nullable=True)