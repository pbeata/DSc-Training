-- the USING clause

USE sql_store;

SELECT
	o.order_id,
    c.first_name,
    s.name AS shipper
FROM orders o
JOIN customers c
	USING (customer_id)  -- only works if the column name is exactly the same in both tables
LEFT JOIN shippers s
	USING (shipper_id);
    
    
SELECT *
FROM order_items oi
JOIN order_item_notes oin
	ON oi.order_id = oin.order_id AND
		oi.product_id = oin.product_id;

SELECT *
FROM order_items oi
JOIN order_item_notes oin
	USING (order_id, product_id);


USE sql_invoicing;

SELECT
	p.date,
    c.name AS client,
    p.amount,
    pm.name AS name
FROM payments p
JOIN clients c
	USING (client_id)
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id;
    
    
-- natural joins (DO NOT USE)

USE sql_store;

SELECT
	o.order_id,
    c.first_name
FROM orders o
NATURAL JOIN customers c;  -- join based on common column names


-- cross joins

SELECT
	c.first_name AS customer,
    p.name as product
FROM customers c
CROSS JOIN products p
ORDER BY c.first_name;

SELECT
	c.first_name AS customer,
    p.name as product
FROM customers c, products p
ORDER BY c.first_name;


SELECT *
FROM shippers s
CROSS JOIN products p;

-- implicit method not recommended
SELECT
	s.name AS shipper,
    p.name AS product
FROM shippers s, products p
ORDER BY s.name;


-- UNIONS: combine records from multiple tables

SELECT
	order_id,
    order_date,
    'Active' AS status
FROM orders
WHERE order_date >= '2019-01-01'
UNION
SELECT
	order_id,
    order_date,
    'Archived' AS status
FROM orders
WHERE order_date < '2019-01-01';

-- combine tables as long as the specified number of columns is the same
SELECT first_name AS all_names
FROM customers
UNION
SELECT name
FROM shippers;

-- bronze: pts < 2000
-- silver: pts = [2000, 3000)
-- gold: pts > 3000

SELECT customer_id, first_name, points, 
	'Bronze' AS type
FROM customers
WHERE points < 2000
UNION
SELECT customer_id, first_name, points, 
	'SILVER' AS type
FROM customers
-- WHERE points >= 2000 AND points < 3000
WHERE points BETWEEN 2000 AND 3000
UNION
SELECT customer_id, first_name, points, 
	'GOLD' AS type
FROM customers
WHERE points >= 3000
ORDER BY first_name;





