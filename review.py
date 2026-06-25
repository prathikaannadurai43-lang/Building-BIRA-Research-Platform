from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("businesses.id"), index=True)
    source = Column(String, index=True)
    rating = Column(Float)
    review_text = Column(String)
    reviewer_name = Column(String)
    review_date = Column(DateTime)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
