from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, User, Role
app = FastAPI()

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
         ),

]


@app.get("/")
def root():
    return {"message": "Hello Ivan"}
