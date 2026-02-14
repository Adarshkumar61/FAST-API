from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "hlo adarsh"}

@app.get("/about")
def about():
    return {"msg": "about page"}

@app.get("/contact")
def contact():
    return {"msg": "contact page"}