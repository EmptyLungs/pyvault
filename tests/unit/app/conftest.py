from unittest.mock import MagicMock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.routers.health import router as health_router
from app.settings import ServerSettings


@pytest.fixture
def fastapi_app_client(settings):
    app = FastAPI()
    app.state.settings = settings

    app.include_router(health_router)

    client = TestClient(app)
    client.headers['Content-Type'] = 'application/json'

    yield app, client


@pytest.fixture
def settings():
    server_settings = ServerSettings(host='127.0.0.1', port=8080, debug=True)
    return MagicMock(
        server=server_settings,
        sentry=MagicMock(),
        logging=MagicMock(),
        postgres=MagicMock(),
    )
