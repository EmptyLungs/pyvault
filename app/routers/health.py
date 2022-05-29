from fastapi.routing import APIRouter
from fastapi.responses import PlainTextResponse


router = APIRouter()


@router.get(
    '/health',
    summary='Healthcheck',
    response_class=PlainTextResponse
)
def health():
    return "Healthy!"
