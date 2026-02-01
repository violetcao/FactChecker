from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from .database import Base

class Claims(Base):
    __tablename__ = "claims"
    id = Column(Integer, primary_key=True)
    fact_string = Column(String, nullable=False)
    fact_status = Column(String, nullable=False)
    date = Column(Integer)
    subjects = Column(String, nullable=False)
    speaker = Column(String, nullable=False)
    job = Column(String, nullable=False)
    context = Column(String, nullable=False)


