from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.rm import sessionmaker
from constants import DB_USER, DB_PASSWORD, DB_URL

DATABASE_URL = 'postgresql://{}:{}@{}/db'.format(DB_USER, DB_PASSWORD, DB_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)
Base = declarative_base()
