CREATE DATABASE bitcount;
\c bitcount;

CREATE TABLE tweetcount
       (timestamp TIMESTAMP PRIMARY KEY NOT NULL,
       tweet TEXT NOT NULL);

CREATE TABLE transactioncount
       (timestamp TIMESTAMP NOT NULL,
       hashkey PRIMARY KEY TEXT NOT NULL);