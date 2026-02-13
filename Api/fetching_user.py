from fastapi import FastAPI

app = FastAPI()

# Home route
@app.get("/")

# Dynamic path parameter route
@app.get("/user/{id}")
def get_user(name : str, id: int):
    return {
        "msg": "successuly read data",
        "name" : name,
        "id": id
    }

# run : #http://127.0.0.1:8000/user/25?name=adarsh 

# http://127.0.0.1:8000/user/99?name=amit  it will show this response:
# {
#     "message": "User fetched successfully",
#     "user_id": 99,
#     "name": "amit"
# }