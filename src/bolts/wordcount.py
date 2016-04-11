from __future__ import absolute_import, print_function, unicode_literals
import psycopg2
from collections import Counter
from streamparse.bolt import Bolt
from datetime import datetime


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
	cur.execute('''DELETE FROM bitcointweet''')
	conn.commit()
	conn.close()
#self.redis = StrictRedis()

    def process(self, tup):
        word2 = [thing.replace("'","").replace("`","").replace(".","") for thing in tup.values[0]]
	#word2 = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        

        # Increment the local count
        #self.counts[word] += 1
        #self.emit([word, self.counts[word]])
	#self.emit([word])
	#self.emit(word2)
	
	#self.log(word2)
	dt = '{:%m/%d/%Y %H:%M:%S}'.format(datetime.now())
        self.log(dt)
	#Save to table
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
	#if self.counts[word] == 1: #First time word appears
	qry = "INSERT INTO bitcointweet (tweets,curr_time) VALUES ('" + ' '.join(word2) + "','" + str(dt) + "');"
	#"INSERT INTO Tweetwordcount (word,count) VALUES ('" + word + "', 1);"
	#"UPDATE Tweetwordcount SET count=%s WHERE word=%s;",(self.counts[word],word))
	cur.execute(qry)
	conn.commit()
	
        #self.log('%s:' % (word))
	#self.log(word2)
	
