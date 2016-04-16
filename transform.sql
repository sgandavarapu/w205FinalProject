CREATE TABLE compare_traffic AS 
(SELECT a.dt as dt, 
       a.hour as hour, 
       COUNT(DISTINCT a.transaction_id) as num_transactions, 
       COUNT(DISTINCT b.tweet) as num_tweets
<<<<<<< HEAD
FROM (SELECT DATE(timestamp) as dt,
             date_part('hour', timestamp) as hour,
             transaction_id
      FROM transactioncount) a
     LEFT JOIN
     (SELECT DATE(timestamp) as dt,
             date_part('hour',timestamp) as hour,
             tweet
      FROM tweetcount) b
     ON a.dt = b.dt AND a.hour = b.hour
=======
FROM transactioncount a
     LEFT JOIN
     tweetcount b
     ON date_part('hour', a.timestamp) = date_part('hour', b.timestamp)
>>>>>>> origin/master
GROUP BY 1,2);
