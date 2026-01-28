SELECT
     EXTRACT(YEAR FROM order_date) AS year,
	 EXTRACT(MONTH FROM order_date) AS month,
	 SUM(amount) AS total_sales
FROM orders
GROUP BY year, month
ORDER BY year, month;