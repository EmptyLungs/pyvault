from pydantic import BaseSettings, BaseModel, Field


class ServerSettings(BaseSettings):
    host: str = Field('127.0.0.1', env='SERVER_HOST')
    port: int = Field(8080, env='SERVER_PORT')
    debug: bool = Field(False, env='DEBUG')


class SentrySettings(BaseSettings):
    dsn: str = Field('', env='SENTRY_DSN')


class LoggingSettings(BaseSettings):
    level: str = Field('info', env='LOG_LEVEL')


class PGSettings(BaseSettings):
    host: str = Field('localhost', env='PG_HOST')
    port: int = Field(5432, env='PG_PORT')
    user: str = Field('postgres', env='PG_USER')
    password: str = Field(..., env='PG_PASSWORD')
    database: str = Field(..., env='PG_DATABASE')

    @property
    def url(self):
        return f'postgres://{self.user}:{self.password}@{self.host}:{self.port}'


class Settings(BaseModel):
    server: ServerSettings
    sentry: SentrySettings
    logging: LoggingSettings
    postgres: PGSettings
