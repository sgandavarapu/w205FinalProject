DROP TABLE IF EXISTS compare_traffic;

CREATE TABLE compare_traffic AS 
(SELECT a.dt as dt, 
       a.hour as hour, 
       COUNT(a.transaction_id) as num_transactions, 
       COUNT(b.tweet) as num_tweets
FROM transactioncount a
     LEFT JOIN
     tweetcount b
     ON a.dt = b.dt AND a.hour = b.hour
GROUP BY 1,2);
