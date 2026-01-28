INSERT INTO customers (customer_id, name, city) VALUES
(1, 'Amit', 'Mumbai'),
(2, 'Riya', 'Chennai'),
(3, 'Karan', 'Vadodara');

INSERT INTO products (product_id, product_name, price) VALUES
(101, 'Laptop', 55000.00),
(102, 'Mouse', 500.00),
(103, 'Keyboard', 1200.00);

INSERT INTO orders (order_id, customer_id, order_date, amount) VALUES
(1001, 1, '2025-01-10', 56200.00),
(1002, 2, '2025-01-11', 1700.00);

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1001, 101, 1),
(1001, 102, 2),
(1002, 103, 1);