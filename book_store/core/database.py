import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

# TODO: lets use arguments from docker container postgres instead of native db
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://bookuser:parola123@localhost:5432/bookstore",  # TODO: seems like hardcoded values, should be moved into configuration file
)

engine = create_engine(DATABASE_URL, echo=True)
metadata = MetaData()
Base = declarative_base(metadata=metadata)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# TODO: name is little bit strange. Should be named as session at least since database is more wide abstraction.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
