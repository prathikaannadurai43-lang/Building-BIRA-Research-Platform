from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class SearchQuery(Base):
    __tablename__ = "search_queries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=True) # Nullable for anonymous searches
    raw_query = Column(String, index=True, nullable=False)
    parsed_business_type = Column(String)
    parsed_location = Column(String)
    status = Column(String, default="pending")
    result_count = Column(Integer, default=0)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
