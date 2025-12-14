from fastapi import APIRouter, HTTPException
from ..Models.user import User
from ..Schemas.user import UserRegister, UserLogin
from ..Core.security import hash_password, verify_password, create_access_token
from ..database import SessionLocal

router = APIRouter(prefix="/api/auth")

@router.post("/register")
def register(user: UserRegister):
    db = SessionLocal()
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    db = SessionLocal()
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.id, "role": db_user.role})
    return {"access_token": token}
