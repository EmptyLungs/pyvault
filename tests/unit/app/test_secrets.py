from fastapi import status


def test_list_secrets(fastapi_app_client):
    app, client = fastapi_app_client
    response = client.get('secrets')
    assert response.status_code == status.HTTP_200_OK


def test_delete_secret(fastapi_app_client):
    app, client = fastapi_app_client
    response = client.delete('secrets/1')
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_create_secret(fastapi_app_client):
    app, client = fastapi_app_client
    response = client.post('secrets')
    assert response.status_code == status.HTTP_201_CREATED
