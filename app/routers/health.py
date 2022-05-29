from fastapi.responses import PlainTextResponse
from fastapi.routing import APIRouter

router = APIRouter()


@router.get('/health', summary='Healthcheck', response_class=PlainTextResponse)
def health():
    return "Healthy!"
