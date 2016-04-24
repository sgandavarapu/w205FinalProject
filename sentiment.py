import psycopg2
import sys
import psycopg2.extras
import csv
from collections import defaultdict

# wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
# sudo easy_install --upgrade pip
# pip install vaderSentiment

def sentiment():
	from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
	conn = psycopg2.connect(database="bitcount", user="postgres", password="w205project", host="ec2-54-175-8-65.compute-1.amazonaws.com", port="5432")
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	qry = "SELECT tweet as message,dt,hour from tweetcount"
	cur.execute(qry)
	
	#sent_out = dict()
	sent_out = defaultdict(list)
	existing_keys =[]
	rows = cur.fetchall()
	for row in rows:
		#print row
		vs = vaderSentiment(row['message'])
		key = str(row['dt'])+ "," + str(row['hour'])
		if key not in existing_keys:
			sent_out[key] = [0.0,0.0,0.0,0.0,0.0]
			sent_out[key][0] = sent_out.get(key,[])[0] + vs['compound']
			sent_out[key][1] = sent_out.get(key,[])[1] + vs['pos']
			sent_out[key][2] = sent_out.get(key,[])[2] + vs['neu']
			sent_out[key][3] = sent_out.get(key,[])[3] + vs['neg']
			sent_out[key][4] = sent_out.get(key,[])[4] + 1.0
			existing_keys.append(key)
		else:
			sent_out[key][0] = sent_out.get(key,[])[0] + vs['compound']
			sent_out[key][1] = sent_out.get(key,[])[1] + vs['pos']
			sent_out[key][2] = sent_out.get(key,[])[2] + vs['neu']
			sent_out[key][3] = sent_out.get(key,[])[3] + vs['neg']
			sent_out[key][4] = sent_out.get(key,[])[4] + 1.0
		#print row['dt'],row['hour'],vs['compound']
		#print key
	return sent_out
		
		#print row['message'],vs['pos'],",",vs['neu'],",",vs['neg']

if __name__ == "__main__":
	sentiment_output = sentiment()
	out_file = sys.argv[1]
	#for keys,values in sentiment_output:
	#	print keys,values
	writer = csv.writer(open(out_file, 'wb'))
	writer.writerow(['dt','hour','compound','positive','neutral','negative'])
	for key, value in sentiment_output.items():
		writer.writerow([key.split(",")[0], key.split(",")[1],value[0]/value[4],value[1]/value[4],value[2]/value[4],value[3]/value[4]])