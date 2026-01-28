SELECT *
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.city = 'Mumbai';
