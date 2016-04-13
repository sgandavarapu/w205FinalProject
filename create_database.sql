CREATE DATABASE bitcount;
\c bitcount;

CREATE TABLE tweetcount
       (timestamp TIMESTAMP PRIMARY KEY NOT NULL,
       tweet TEXT NOT NULL);

CREATE TABLE transactioncount
       (timestamp TIMESTAMP NOT NULL,
       hashkey TEXT NOT NULL,
       transaction_id TEXT NOT NULL);
