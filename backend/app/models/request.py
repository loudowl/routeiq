from sqlalchemy import Column, Integer, String, Float, DateTime
from ..database import Base

class RequestLog(Base):
    __tablename__ = 'request_logs'

    id = Column(Integer, primary_key=True, index=True)
    model_used = Column(String)
    tokens = Column(Integer)
    latency = Column(Float)
    estimated_cost = Column(Float)
    timestamp = Column(DateTime)
