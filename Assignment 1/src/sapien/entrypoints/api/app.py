from fastapi import APIRouter, FastAPI

from sapien.entrypoints.api.routes.healthcheck import router as healthcheck_router
from sapien.entrypoints.api.routes.search import router as search_router

app = FastAPI(
    title="My Search Engine", swagger_ui_parameters={"operationsSorter": "alpha"}, prefix="/api/v1"
)

# main API router
api_router = APIRouter(prefix="/api/v1")
api_router.include_router(healthcheck_router)
api_router.include_router(search_router)

# app
app.include_router(api_router)
