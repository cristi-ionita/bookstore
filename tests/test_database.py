from sqlalchemy import text

from book_store.core.database import engine


def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        scalar = result.scalar()
        assert scalar == 1
