from book_store.users.domain.database import metadata, database
from sqlalchemy import create_engine

engine = create_engine(str(database.url))
metadata.create_all(engine)