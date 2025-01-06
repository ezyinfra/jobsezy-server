from sqlalchemy.orm import Session
from app.models.admin_login import AdminLogin
from app.schemas.admin import AdminCreate

async def creating_admin(db: Session, admin: AdminCreate):
    db_admin = AdminLogin(uname = admin.username, password = admin.password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


# Get admin by username (optional, for validation purposes)
async def get_admin_by_username(db: Session, username: str):
    return db.query(AdminLogin).filter(AdminLogin.uname == username).first()