from sqlalchemy import create_engine
from book_store.users.domain.database import metadata


DATABASE_URL = "postgresql://bookuser:parola123@localhost:5432/bookstore"

engine = create_engine(DATABASE_URL)

metadata.create_all(engine)

print("Created!")
