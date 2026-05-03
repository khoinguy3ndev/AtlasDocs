from fastapi import APIRouter

from app.schemas.health import HealthResponse

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("", response_model=HealthResponse, summary="Health check")
def health_check() -> HealthResponse:
    """Return the current health status of the server."""
    return HealthResponse(status="ok", message="Server is running")
