
DROP TABLE IF EXISTS crudeoilprice;
DROP TABLE IF EXISTS quandlgoldprice;
DROP TABLE IF EXISTS quandlcopperprice;
DROP TABLE IF EXISTS quandlsilverprice;
DROP TABLE IF EXISTS quandlbitcoinprice;

CREATE TABLE crudeoilprice
       (date DATE NOT NULL,
       oilValue DECIMAL NOT NULL);

CREATE TABLE quandlgoldprice
              (date DATE NOT NULL,
              goldValue DECIMAL NOT NULL);

CREATE TABLE quandlcopperprice
              (date DATE NOT NULL,
              copperValue DECIMAL NOT NULL,
              copperHigh TEXT,
              copperLow TEXT,
              copperVolume TEXT,
              copperLastClose TEXT,
              copperChange TEXT,
              copperVar TEXT);

CREATE TABLE quandlsilverprice
             (date DATE NOT NULL,
             silverUSDValue DECIMAL,
             silverGBPValue TEXT,
             silverEuroValue TEXT);

CREATE TABLE quandlbitcoinprice
              (date DATE NOT NULL,
              bitcoinAverage DECIMAL NOT NULL,
              askPrice TEXT,
              bidPrice TEXT,
              lastPrice TEXT,
              totalVolume TEXT NOT NULL);

\COPY crudeoilprice FROM '/root/quandlcrudeoilData.csv' DELIMITER ',' CSV HEADER
\COPY quandlgoldprice FROM '/root/quandlgoldData.csv' DELIMITER ',' CSV HEADER
\COPY quandlcopperprice FROM '/root/quandlcopperData.csv' DELIMITER ',' CSV HEADER
\COPY quandlsilverprice FROM '/root/quandlsilverData.csv' DELIMITER ',' CSV HEADER
\COPY quandlbitcoinprice FROM '/root/bitcoindata.csv' DELIMITER ',' CSV HEADER
