CREATE DATABASE bitcount;
\c bitcount;

CREATE TABLE tweetcount
       (timestamp TIMESTAMP NOT NULL,
       tweet TEXT NOT NULL,
       dt DATE,
       hour SMALLINT);

CREATE TABLE transactioncount
       (timestamp TIMESTAMP NOT NULL,
       hashkey TEXT NOT NULL,
       transaction_id TEXT NOT NULL,
       dt DATE,
       hour SMALLINT);