DROP TABLE IF EXISTS commodity_consolidate;
CREATE TABLE commodity_consolidate AS
(SELECT crudeoilprice.date, crudeoilprice.oilValue, quandlgoldprice.goldValue,
  quandlcopperprice.copperValue, quandlsilverprice.silverUSDValue, quandlbitcoinprice.bitcoinAverage
 FROM crudeoilprice, quandlgoldprice, quandlcopperprice, quandlsilverprice, quandlbitcoinprice
 WHERE crudeoilprice.date = quandlgoldprice.date AND crudeoilprice.date = quandlcopperprice.date
 AND crudeoilprice.date = quandlsilverprice.date AND crudeoilprice.date = quandlbitcoinprice.date );
