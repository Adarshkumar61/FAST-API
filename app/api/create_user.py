from fastapi import FastAPI

app = FastAPI()

@app.post('/create_user')

def create_user(name: str, age: int):
    return {
        "msg":"user created successfully",
        "name": name,
        "age": age
    }


# run : http://127.0.0.1:8000/docs
# click try it out
