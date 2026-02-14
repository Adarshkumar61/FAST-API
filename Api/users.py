# #code for showing optional parameters in the url
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional

# app = FastAPI()

# class User(BaseModel):
#     name : str
#     age : Optional[int] = None
#     phone_number : Optional[str] = None

# @app.post("/create_user")
# def create_user(user: User):
#     return {
#         "msg": "msg successfully loaded",
#         "data": user.model_dump()
#     }


# Response Model:


# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()
# class User(BaseModel):
#     name: str
#     age: int
#     password: int

# class User_response(BaseModel):
#     name: str
#     age: int

# @app.post("/create_user", response_model= User_response)

# def create_user(user:User):
#     return user.model_dump()

# Update endpoint example:

from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()
db = {}
class User(BaseModel):
    name : str
    age : int

@app.post("/create_user/{user_id}")

def create_user(user_id: int, user : User):
    db[user_id] = user
    return {
        "msg": "msg created successfully",
        "data": db
    }

@app.put("/update_user/{user_id}")
def updated_user(user_id: int, user : User):
    if user_id in db:
        db[user_id] = user
        return {"msg": "updated successfully","data": db}
    return {"msg": "user not found"}
        
@app.delete("/delete_user/{user_id}")

def delete_user(user_id : int):
    if user_id in db:
        del db[user_id]
        return {
            "msg": "user deleted successfully",
            "data": db}
    return {"msg": "user not found"}
