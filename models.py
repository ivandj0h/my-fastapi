import enum
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum


class Gender(str, enum):
    male = "Male"
    female = "Female"


class Role(str, enum):
    admin: "Admin"
    user: "User"


class UserBase(BaseModel):
    id: Optional[UUID] = uuid4
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]
