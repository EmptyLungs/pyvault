import sentry_sdk
import uvicorn
from fastapi import FastAPI
from tortoise import Tortoise

from .configure import get_settings
from .routers.health import router as health_router

settings = get_settings()

app = FastAPI(debug=settings.server.debug)
app.state.settings = settings

if sentry_dsn := settings.sentry.dsn:
    sentry_sdk.init(sentry_dsn)

app.include_router(health_router)


@app.on_event('startup')
async def init_tortoise():
    await Tortoise.init(db_url=settings.postgres.url, modules=dict(models=['app.models']))
    await Tortoise.generate_schemas()


@app.on_event("shutdown")
async def shutdown():
    await Tortoise.close_connections()


if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host=settings.server.host,
        port=settings.server.port,
        proxy_headers=True,
        forwarded_allow_ips='*',
        http="h11",
    )
