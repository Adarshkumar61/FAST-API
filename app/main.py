# from fastapi import FastAPI

# from app.db import models  # noqa: F401 - ensure models are imported before create_all
# from app.db.database import Base, engine

# app = FastAPI()

# Base.metadata.create_all(bind=engine)


from fastapi import FastAPI
from app.api.user_routes import router
from app.db.database import engine
from app.db import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
