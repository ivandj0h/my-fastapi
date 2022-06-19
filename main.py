from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, User, Role
app = FastAPI()

# The Models
db: List[User] = [
    User(id=uuid4(),
         first_name="Admin",
         last_name="Application",
         gender=Gender.female,
         roles=[Role.user]
         ),
    User(id=uuid4(),
         first_name="Super",
         last_name="Admin",
         gender=Gender.male,
         roles=[Role.admin, Role.user]
         )

]

# The Endpoints


@app.get("/")
async def root():
    return {"message": "Hello Ivan"}


@app.get("/api/v1/users")
async def get_all_users():
    return db


@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return user
