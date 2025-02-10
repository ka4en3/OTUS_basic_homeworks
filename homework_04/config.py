convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

db_async_url = "postgresql+asyncpg://user:password@localhost:5432/db"
# db_sync_url = "postgresql+psycopg://user:password@localhost:5432/db"
db_echo = True