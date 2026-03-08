from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255), nullable=False)

    jobs = relationship("Job", back_populates="owner")

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(255))
    role = Column(String(255))
    status = Column(String(50), default="Applied")
    notes = Column(String(500))

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="jobs")