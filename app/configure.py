from functools import lru_cache

from .settings import LoggingSettings, PGSettings, SentrySettings, ServerSettings, Settings


@lru_cache(maxsize=None)
def get_settings() -> Settings:
    return Settings(server=ServerSettings(), sentry=SentrySettings(), logging=LoggingSettings(), postgres=PGSettings())
