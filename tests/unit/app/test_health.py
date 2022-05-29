def test_health(fastapi_app_client):
    app, client = fastapi_app_client
    response = client.get('/health')
    assert response.text == "Healthy!"
