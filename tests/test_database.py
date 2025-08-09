from sqlalchemy import text

from book_store.core.database import engine

# TODO: Try answer on question what kind of test is it? Do we need it in same forlder with all tests?
# TODO: maybe we should mark this test somehow?


def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        scalar = result.scalar()
        assert scalar == 1
