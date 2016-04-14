CREATE TABLE compare_traffic AS 
(SELECT DATE(a.timestamp) as dt, 
       date_part('hour', a.timestamp) as hour, 
       COUNT(DISTINCT a.transaction_id) as num_transactions, 
       COUNT(DISTINCT b.tweet) as num_tweets
FROM transactioncount a
     LEFT JOIN
     tweetcount b
     ON date_part('hour', a.timestamp) = date_part('hour', b.timestamp)
GROUP BY 1,2);
