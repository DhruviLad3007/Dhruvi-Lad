CREATE TABLE products (
    product_id INT PRIMARY KEY,
	product_name VARCHAR(100),
	price NUMERIC(10,2)	
);

CREATE TABLE order_items (
    order_id INT,
	product_id INT,
	quantity INT,
	FOREIGN KEY (order_id) REFERENCES
orders(order_id),
    FOREIGN KEY (product_id) REFERENCES
products(product_id)
);