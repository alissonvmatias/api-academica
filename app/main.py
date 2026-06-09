from fastapi import FastAPI
from app.routes.routes import router
from app.database.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Gestão Acadêmica")

app.include_router(router)
