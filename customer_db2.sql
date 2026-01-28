INSERT INTO customers (customer_id, name, city, email) VALUES
(101, 'Rahul Sharma', 'Mumbai', 'rahul@gmail.com'),
(102, 'Priya Patel', 'Ahmedabad', 'priya@gmail.com'),
(103, 'Amit Verma', 'Delhi', 'amit@gmail.com'),
(104, 'Sneha Iyer', 'Chennai', 'sneha@gmail.com'),
(105, 'Neha Singh', 'Mumbai', 'neha@gmail.com');

INSERT INTO orders (order_id, order_date, amount, customer_id) VALUES
(1, '2024-01-10', 2500.00, 101),
(2, '2024-01-12', 1800.50, 102),
(3, '2024-01-15', 3200.75, 101),
(4, '2024-01-20', 1500.00, 103),
(5, '2024-01-22', 2750.25, 105);
