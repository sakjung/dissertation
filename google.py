# -*- coding: utf-8 -*-
"""
Created on Fri May 22 01:02:01 2020

@author: yuaa6
"""
import requests
import json
import sys
from math import ceil
from numpy import random
from time import sleep
import logging
from google_play_scraper import Sort, reviews
from google_play_scraper import app
import base64
from dateutil.parser import parse
from sqlalchemy import *
# tidal google play id: com.aspiro.tidal

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

def get_reviews_count():

    number_of_reviews = app(
    'com.aspiro.tidal',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
    )["reviews"]

    return number_of_reviews

def etl_google(number_of_reviews, fetch_size=100):

    continuation_token = None
    total_reviews_scraped = 0
    with engine.connect() as conn:
        for i in range(0,ceil(number_of_reviews/fetch_size)):
            this_data = []
            logging.info("This is {}th request".format(int(i+1)))

            # fetch data from google play store
            try:
                result, continuation_token = reviews(
                    'com.aspiro.tidal',
                    lang='en', # defaults to 'en'
                    country='us', # defaults to 'us'
                    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
                    continuation_token=continuation_token,
                    count=fetch_size
                )
                logging.info("Retrieved total {} reviews so far".format(int(len(result))))

            except Exception as e:
                logging.error("Failed to request data:" + str(e))
                sys.exit(1)

            # transform data
            for review in result:
                data = {
                    'id': None,
                    'username': review["userName"],
                    'date': parse(str(review["at"])).date(),
                    'rating': review["score"],
                    'origin': 2,
                    'review': review["content"]
                }

                this_data.append(data)

            # move data to sqlite
            conn.execute(reviews_table.insert(), this_data)

            total_reviews_scraped += int(len(this_data))
            logging.info("Total {} reviews has been moved to db so far!".format(total_reviews_scraped))

            randomNum = random.uniform(1, 3)
            logging.info("Sleeping for {}".format(randomNum))
            sleep(randomNum)

if __name__=="__main__":
    number_of_reviews = get_reviews_count()
    print(number_of_reviews)
    sys.exit(0)
    engine = create_engine('sqlite:///appstore.db')
    etl_google(number_of_reviews)
    engine.dispose()
