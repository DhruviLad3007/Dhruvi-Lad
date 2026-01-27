CREATE VIEW user_order_summary AS 
SELECT
    u.user_id,
	u.name,
	u.email,
	COUNT(o.order_id) AS total_orders,
	SUM(o.amount) AS total_amount
FROM users u
LEFT JOIN orders o
ON u.user_id = o.user_id
GROUP BY u.user_id, u.name, u.email;

