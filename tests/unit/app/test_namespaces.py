from fastapi import status


def test_list_namespaces(fastapi_app_client):
    app, client = fastapi_app_client
    response = client.get('namespaces')
    assert response.status_code == status.HTTP_200_OK


def test_delete_namespaces(fastapi_app_client):
    app, client = fastapi_app_client
    response = client.delete('namespaces/1')
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_create_namespaces(fastapi_app_client):
    app, client = fastapi_app_client
    response = client.post('namespaces')
    assert response.status_code == status.HTTP_201_CREATED
