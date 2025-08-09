import pytest
from fastapi.testclient import TestClient

from book_store.app import app
from book_store.core.database import Base, engine


@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # FIXME: Do we have separate config for tests with db like testdb?
    # FIXME: righ now we create and delete our main db and it is not good
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client():
    return TestClient(app)
