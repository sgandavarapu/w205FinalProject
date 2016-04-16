mport psycopg2
import sys
import psycopg2.extras

# wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
# sudo easy_install --upgrade pip
# pip install vaderSentiment

def sentiment():
	from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
	conn = psycopg2.connect(database="bitcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	qry = "SELECT (tweet->'text') as message from tweetcount"
	cur.execute(qry)

	rows = cur.fetchall()
	for row in rows:
		vs = vaderSentiment(row['message'])
		print row['message'],",",vs['compound']
		print vs['pos'],",",vs['neu'],",",vs['neg']

if __name__ == "__main__":
	sentiment()
