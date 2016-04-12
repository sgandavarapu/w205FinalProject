from __future__ import absolute_import, print_function, unicode_literals

import re
from streamparse.bolt import Bolt

################################################################################
# Function to check if the string contains only ascii chars
################################################################################
def ascii_string(s):
  return all(ord(c) < 128 for c in s)

class ParseTweet(Bolt):

    def process(self, tup):
        tweet = tup.values[0]  # extract the tweet

        # Split the tweet into words

        words = tweet.split()
	valid_words = []
	
	#Filter out tweets that do not have word of interest
	if 'bitcoin' in words or 'Bitcoin' in words or 'BITCOIN' in words or 'BitCoin' in words or '#bitcoin' in words or 'bit coin' in words:
        	
		# Filter out the hash tags, RT, @ and urls
	               	
		for word in words:

        	    # Filter the hash tags
	            #if word.startswith("#"): continue

        	    # Filter the user mentions
	            if word.startswith("@"): continue

        	    # Filter out retweet tags
	            if word.startswith("RT"): continue

        	    # Filter out the urls
	            if word.startswith("http"): continue

        	    # Strip leading and lagging punctuations
            	    aword = word.strip("\"?><,'.:;)")
	
        	    # now check if the word contains only ascii
	            if len(aword) > 0 and ascii_string(word):
        	        valid_words.append(aword)

        if not valid_words: return

        # Emit all the words
        self.emit([valid_words])
	self.log(valid_words)
        # tuple acknowledgement is handled automatically
