from fastapi import FastAPI
from app.routes import router
from app.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(router, prefix=settings.API_V1_STR)

@app.on_event("startup")
def on_startup():
    from app.dependencies import engine
    from app.models import Base
    Base.metadata.create_all(bind=engine)

