from pydantic import BaseModel
from typing import Optional
import datetime


class RoleCreate(BaseModel):
    name: str

class RoleRead(RoleCreate):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class PermissionCreate(BaseModel):
    name: str

class PermissionRead(PermissionCreate):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    password: str
    role_id: Optional[int] = None

class UserRead(UserCreate):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int

class PostRead(PostCreate):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True
