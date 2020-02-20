from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)
from sqlalchemy.sql import func

from databases import Database

DATABASE_URI = 'postgresql://movie_user:movie_password@localhost/movie_db'

engine = create_engine(DATABASE_URI)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(String))
)

database = Database(DATABASE_URI)