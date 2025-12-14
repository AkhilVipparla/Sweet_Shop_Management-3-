from fastapi import APIRouter, HTTPException
from ..database import SessionLocal
from ..Models.sweet import Sweet
from ..Core.dependencies import get_current_user
from ..Models.user import User
from sqlalchemy.orm import Session
from fastapi import Depends


router = APIRouter(prefix="/api/sweets")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{id}/purchase")
def purchase_sweet(
    id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    sweet = db.query(Sweet).with_for_update().filter(Sweet.id == id).first()

    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    if sweet.quantity <= 0:
        raise HTTPException(status_code=400, detail="Out of stock")

    sweet.quantity -= 1
    db.commit()

    return {"message": "Purchase successful"}

