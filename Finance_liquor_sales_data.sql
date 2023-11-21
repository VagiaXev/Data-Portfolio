USE liquor_sales;

SELECT * 
FROM finance_liquor_sales
WHERE date LIKE "2016%"
OR date LIKE "2017%"
OR date LIKE "2018%"
OR date LIKE "2019%"
ORDER BY date;