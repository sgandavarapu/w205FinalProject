(ns bitcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn bitcount [options]
   [
    ;; spout configuration
    {"tweet-spout" (python-spout-spec
          options
          "spouts.tweets.Tweets"
          ["tweet"]
          )
     "transaction-spout" (python-spout-spec
          options
          "spouts.transactions.Transactions"
          ["response_dict"]
          )
    }
    ;; bolt configuration
    {"parse-tweet-bolt" (python-bolt-spec
          options
          {"tweet-spout" :shuffle}
          "bolts.parse.ParseTweet"
          ["tweet"]
          )
     "count-bolt" (python-bolt-spec
          options
          {"parse-tweet-bolt" ["tweet"]}
          "bolts.tweetcount.TweetCounter"
          ["tweet" "dt"]
	  )
     "transaction-bolt" (python-bolt-spec
          options
          {"transaction-spout" :shuffle}
          "bolts.transactionlogger.TransactionLogger"
          ["timestamp", "hashkey"])
     
    }
  ]
)
