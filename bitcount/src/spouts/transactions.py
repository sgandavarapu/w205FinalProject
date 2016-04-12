from __future__ import absolute_import,print_function, unicode_literals
from streamparse.spout import Spout
import urllib2
import json
from blockchain import blockexplorer
import time

class Transactions(Spout):
    def initialize(self, stormconf, context):
        1==1
        
    def next_tuple(self):
        time.sleep(0.1)
        response_dict = blockexplorer.get_latest_block()
        self.emit([(response_dict.hash, response_dict.time)])
        
    def ack(self, tup_id):
        pass # if a tuple is processed properly, do nothing
    
    def fail(self, tup_id):
        pass # if a tuple fails to process, do nothing
