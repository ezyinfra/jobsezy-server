import os
from fastapi import APIRouter, Depends, Request , HTTPException 
from app.database.database import get_db
from sqlalchemy.orm import Session
from app import schemas, crud
from app.schemas.admin import AdminCreate
from app.crud.admin_login import creating_admin , get_admin_by_username
from app.database.database import SessionLocal

router = APIRouter()

@router.post("/admin/saveLoginInfo")
async def create_admin(admin: AdminCreate , db: Session = Depends(get_db)):
    try:
        db_admin = await get_admin_by_username(db, admin.username)
        if db_admin:
            raise HTTPException(status_code=400, detail="Username already registered")

        created_admin = creating_admin(db=db, admin=admin)  # No await here; it's not async
        return {"message": "Admin account created successfully"}
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred")