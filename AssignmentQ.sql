USE `liquorSales`;
DESCRIBE finance_liquor_sales;
SELECT * FROM finance_liquor_sales
WHERE YEAR(date) BETWEEN 2016 AND 2019
ORDER BY date;