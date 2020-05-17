# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:11:58 2020

@author: yuaa6
"""
import requests
import json
import sys
from numpy import random
from time import sleep
from sqlalchemy import *
import logging
from dateutil.parser import parse
from math import ceil

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

def etl_apple(number_of_reviews):
    headers = {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldlYlBsYXlLaWQifQ.eyJpc3MiOiJBTVBXZWJQbGF5IiwiaWF0IjoxNTg4OTEyMDA1LCJleHAiOjE2MDQ0NjQwMDV9.TWF75lk72kCfAeUn9Hv1GYvD3InqFafYLcsTo4-2hxbcYRqnDZuUaqLAxLziIC-mgE7bNOq8goC_LCh7kvxacw',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://apps.apple.com',
                'pragma': 'no-cache',
                'referer': 'https://apps.apple.com/us/app/tidal-music/id913943275',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
            }

    offset = 0
    with engine.connect() as conn:
        # with conn.begin() as transaction:
        for i in range(0,ceil(number_of_reviews/10)):
            this_data = []
            logging.info("This is {}th request. Scraping from {} to {}".format(ceil((offset+10)/10), int(offset+1), offset+10))
            url = 'https://amp-api.apps.apple.com/v1/catalog/us/apps/913943275/reviews?l=en-US&offset={}&platform=web&additionalPlatforms=appletv%2Cipad%2Ciphone%2Cmac'.format(offset)

            # extract data
            try:
                res = requests.get(url=url,
                headers=headers)
            except:
                logging.error(res.text)
                sys.exit(1)


            logging.info("Requests Successful!")

            raw = json.loads(res.text)
            logging.info("Retrieved {} reviews".format(int(len(raw['data']))))

            for i in range(0,int(len(raw['data']))):
                data = {
                    'id': None,
                    'username': raw['data'][i]['attributes']['userName'],
                    'date': parse(raw['data'][i]['attributes']['date']).date(),
                    'rating': raw['data'][i]['attributes']['rating'],
                    'origin': 1,
                    'review': raw['data'][i]['attributes']['review']
                }

                this_data.append(data)

            # move data to sqlite
            # using this_data

            try:
                conn.execute(reviews_table.insert(), this_data)
            except Exception as e:
                logging.error(str(e))
                sys.exit(1)

            offset += int(len(raw['data']))

            randomNum = random.uniform(1, 3)
            logging.info("Sleeping for {}".format(randomNum))
            sleep(randomNum)

if __name__=="__main__":
    engine = create_engine('sqlite:///appstore.db')
    # 10665 reviews exist
    etl_apple(10670)
    engine.dispose()
