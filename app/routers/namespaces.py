from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

router = APIRouter(prefix='/namespaces')


@router.get(
    '',
    summary='Returns list of namespaces',
    response_class=JSONResponse,
)
def list_namespaces():
    return JSONResponse(status_code=status.HTTP_200_OK, content={})


@router.post(
    '',
    summary='Creates namespace',
    response_class=JSONResponse,
)
def create_namesace():
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={})


@router.delete(
    '/{namespace_id}',
    summary='Deletes namespace',
    response_class=JSONResponse,
)
def delete_namespace(namespace_id: int):
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={})
