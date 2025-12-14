from sqlalchemy import Column, String, Float, Integer
from app.database import Base
import uuid

class Sweet(Base):
    __tablename__ = "sweets"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
