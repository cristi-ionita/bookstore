import os
from databases import Database
from sqlalchemy import MetaData

"""URL-ul de conexiune la baza de date PostgreSQL"""
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://bookuser:parola123@localhost:5432/bookstore"
)

"""Obiectul metadata pentru SQLAlchemy (definirea tabelelor)"""
metadata = MetaData()

"""Obiectul Database pentru conexiuni asincrone cu baza de date"""
database = Database(DATABASE_URL)