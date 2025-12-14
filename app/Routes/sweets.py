from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..Models.sweet import Sweet
from ..Schemas.sweet import SweetCreate
from ..Core.dependencies import get_current_user
from ..Models.user import User

router = APIRouter(prefix="/api/sweets", tags=["Sweets"])


# Dependency for DB session (BEST PRACTICE)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ ADD SWEET (JWT PROTECTED - ADMIN ONLY)
@router.post("/")
def add_sweet(
    sweet: SweetCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin only")

    new_sweet = Sweet(**sweet.dict())
    db.add(new_sweet)
    db.commit()
    db.refresh(new_sweet)

    return new_sweet


# ✅ GET SWEETS (JWT PROTECTED - ANY LOGGED USER)
@router.get("/")
def get_sweets(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Sweet).all()
