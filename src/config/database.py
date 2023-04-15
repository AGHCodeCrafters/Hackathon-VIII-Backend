from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
# from dotenv import load_dotenv

# load_dotenv()

SQLALCHEMY_DATABASE_URL = 'postgresql://zwnpiozy:aOmddt1NeL11g6ChW1JPG9HjxmSX3rRH@mahmud.db.elephantsql.com/zwnpiozy'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()