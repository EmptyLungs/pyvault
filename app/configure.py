from functools import lru_cache

from .settings import Settings, PGSettings, LoggingSettings, ServerSettings, SentrySettings


@lru_cache(maxsize=None)
def get_settings() -> Settings:
    return Settings(
        server=ServerSettings(),
        sentry=SentrySettings(),
        logging=LoggingSettings(),
        postgres=PGSettings()
    )
