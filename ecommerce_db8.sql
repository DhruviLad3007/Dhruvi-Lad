SELECT customer_id, SUM(amount) AS total_purchase
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 50000;