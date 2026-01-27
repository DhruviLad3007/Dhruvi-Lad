CREATE TABLE orders (
    order_id INT PRIMARY KEY,
	user_id INT,
	order_date DATE,
	amount DECIMAL(10,2),
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);