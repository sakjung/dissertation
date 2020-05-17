import sys
import requests
import json
import logging
from math import ceil
from numpy import random
from time import sleep
from google_play_scraper import app
from google_play_scraper import Sort, reviews
from random import randint
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *
from dateutil.parser import parse

metadata = MetaData()
reviews_table = Table('reviews', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('username', String),
        Column('date', DateTime),
        Column('rating', Float),
        Column('origin', SMALLINT),
        Column('review', Text)
        )

logger = logging.getLogger()
logger.setLevel(logging.INFO)

engine = create_engine('sqlite:///appstore_test.db', echo=True)
with engine.connect() as conn:
    # delete all rows in reviews_table
    conn.execute(reviews_table.delete())
    # check if the table is empty
    s = select([reviews_table])
    check = conn.execute(s)
    print(check.fetchone())

engine.dispose()
