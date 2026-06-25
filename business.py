from sqlalchemy import Column, Integer, String, Float, JSON, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base

class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    address = Column(String)
    city = Column(String, index=True)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    
    phone = Column(String)
    email = Column(String)
    website = Column(String)
    
    business_type = Column(String, index=True)
    category = Column(String)
    
    latitude = Column(Float)
    longitude = Column(Float)
    
    trust_score = Column(Float, default=0.0)
    security_score = Column(Float, default=0.0)
    fraud_risk = Column(String, default="Low")
    
    verification_count = Column(Integer, default=0)
    is_verified = Column(Boolean, default=False)
    
    services = Column(JSON, default=list)
    working_hours = Column(JSON, default=dict)
    social_profiles = Column(JSON, default=dict)
    source_data = Column(JSON, default=dict)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
