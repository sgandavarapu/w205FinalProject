from __future__ import absolute_import, print_function, unicode_literals
import psycopg2
from collections import Counter
from streamparse.bolt import Bolt
from datetime import datetime


class TweetCounter(Bolt):

    def initialize(self, conf, ctx):
        1==1  

    def process(self, tup):
        tweet = tup.values[0]
	dt = '{:%m/%d/%Y %H:%M:%S}'.format(datetime.now())

        #Save to table
	conn = psycopg2.connect(database="bitcount", user="postgres", password="w205project", host="localhost", port="5432")
        cur = conn.cursor()
	cur.execute("INSERT INTO tweetcount (timestamp, tweet, dt, hour) VALUES ('%s','%s', DATE('%s'), date_part('hour', CAST('%s' as timestamp)))" % (dt, tweet.replace("'",""), dt, dt))
	conn.commit()
	self.emit([tweet,dt])
        self.log('%s: %s' % (tweet, dt))
	
