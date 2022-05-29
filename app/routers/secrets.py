from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

router = APIRouter(prefix='/secrets')


@router.get(
    '',
    summary='Returns list of secrets',
    response_class=JSONResponse,
)
def list_secrets():
    return JSONResponse(status_code=status.HTTP_200_OK, content={})


@router.post(
    '',
    summary='Creates secret',
    response_class=JSONResponse,
)
def create_secret():
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={})


@router.delete(
    '/{secret_id}',
    summary='Deletes secret',
    response_class=JSONResponse,
)
def delete_secret(secret_id: int):
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={})
