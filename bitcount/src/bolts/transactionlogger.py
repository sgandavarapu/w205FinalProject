from __future__ import absolute_import, print_function, unicode_literals
from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
import datetime
from blockchain import blockexplorer

class TransactionLogger(Bolt):
    
    def initialize(self, conf, ctx):
        1==1
        
    def process(self, tup):
        response_dict = tup.values[0]
        hashkey = response_dict[0]
        timestamp = datetime.datetime.fromtimestamp(response_dict[1]).strftime('%Y-%m-%d %H:%M:%S')
        transactions = response_dict[2]
        conn = psycopg2.connect(database="bitcount", user="postgres", password="w205project", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute("SELECT count(timestamp) FROM transactioncount WHERE hashkey='%s'" % (hashkey))
        tcount = cur.fetchone()[0]
        if tcount==0:
            for transaction in transactions:
                cur.execute("INSERT INTO transactioncount (timestamp, hashkey, transaction_id, dt, hour) VALUES ('%s', '%s', '%s', DATE('%s'), date_part('hour', CAST('%s' AS timestamp)))" % (timestamp, hashkey, str(transaction), timestamp, timestamp))
                conn.commit()
        self.emit([timestamp, hashkey, len(transactions)])
        # Log the count - just to see the topology running
        self.log('%s: %s transaction num: %d' % (hashkey, timestamp, len(transactions)))

            
