from pydantic import BaseModel, EmailStr
from typing import Optional


# ---------- User Schemas ----------

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True

# ---------- Token Schema ----------

class Token(BaseModel):
    access_token: str
    token_type: str


# ---------- Job Schemas ----------

class JobCreate(BaseModel):
    company: str
    role: str
    status: Optional[str] = "Applied"
    notes: Optional[str] = None


class JobResponse(BaseModel):
    id: int
    company: str
    role: str
    status: str
    notes: Optional[str]

    class Config:
        from_attributes = True