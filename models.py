from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum


class Gender(str, Enum):
    male = "Male"
    female = "Female"


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]


class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]
