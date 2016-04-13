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
        tweet = tup.values[0].strip("\"?><,'.:;)")  # extract the tweet       
        if 'bitcoin'.upper() in tweet.upper() and ascii_string(tweet):
          # Emit tweets which contain the word bitcoin
            self.emit([tweet])

