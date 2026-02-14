from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
    "status": "success",
    "user": "adarsh",
    "id": 10
}

#     # 
    # return {"message": "File created in static folder"}
    # print("File created in static folder")



#Api → folder name

# intro → file name

# app → FastAPI object name

# --reload → auto restart when file changes
# uvicorn intro:app --reload
#you can also use Api.intro:app 
# but it will not refresh the page when you make changes to the code,
#  so you have to restart the server manually.

# so better to Use uvicorn intro:app --reload


