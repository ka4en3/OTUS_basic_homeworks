from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class DbConfig(BaseModel):
    host: str = "localhost"
    port: int = 5432
    database: str = "db"
    user: str = "user"
    password: str = "password"
    echo: bool = False
    pool_size: int = 50
    max_overflow: int = 0

    @property
    def db_credentials(self) -> str:
        return f"{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    @property
    def url(self) -> str:
        return f"postgresql+psycopg://{self.db_credentials}"

    @property
    def async_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_credentials}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter="__",
    )
    db: DbConfig = DbConfig()


settings = Settings()
