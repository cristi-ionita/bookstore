from databases import Database
from sqlalchemy import MetaData

DATABASE_URL = "postgresql://bookuser:parola123@localhost:5432/bookstore"
database = Database(DATABASE_URL)
metadata = MetaData()
