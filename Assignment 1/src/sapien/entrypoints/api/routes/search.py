"""Search endpoints."""

from fastapi import APIRouter

from sapien.entrypoints.api.model import SearchResponse

router = APIRouter(prefix="/search", tags=["search engine"])


@router.get("/")
def search(query: str, num_results: int = 10) -> SearchResponse:
    return SearchResponse(results=[])
