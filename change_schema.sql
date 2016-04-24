CREATE TABLE tweetcount_new AS
(SELECT *, DATE(timestamp) as dt, date_part('hour',timestamp) as hour
 FROM tweetcount);

CREATE TABLE transactioncount_new AS
(SELECT *, DATE(timestamp) as dt, date_part('hour',timestamp) as hour
 FROM transactioncount);

ALTER TABLE tweetcount RENAME TO tweetcount_old;
ALTER TABLE transactioncount RENAME TO transactioncount_old;

ALTER TABLE tweetcount_new RENAME TO tweetcount;
ALTER TABLE transactioncount_new RENAME TO transactioncount;
