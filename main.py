from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Gender, User, Role, UserUpdateRequest
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
async def get_users():
    return db


@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return user


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted"}
    raise HTTPException(
        status_code=404, detail=f"User with id: {user_id} does not exist!")
