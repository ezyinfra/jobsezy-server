from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.models.mixins import Timestamp 

class AdminLogin( Base, Timestamp):
    __tablename__ = 'admin_login'

    id = Column(Integer, primary_key=True, index=True)
    uname = Column(String, index=True, nullable=False)
    password = Column(String, nullable=False)