
-- INNER JOIN

SELECT order_id, orders.customer_id, first_name, last_name
FROM orders
JOIN customers 
	ON orders.customer_id = customers.customer_id;
    
SELECT order_id, o.customer_id, first_name, last_name
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id;
    
SELECT order_id, p.product_id, quantity, oi.unit_price
FROM order_items oi
JOIN products p 
ON oi.product_id = p.product_id;

-- joining across databases

USE sql_inventory;

SELECT *
FROM store.order_items oi
JOIN products p
	ON oi.product_id = p.product_id;
    
-- self joins

USE sql_hr;

SELECT 
	e.employee_id,
    e.first_name,
    m.first_name AS manager
FROM employees e
JOIN employees m  -- need to use a different alias (m)
	ON e.reports_to = m.employee_id;
    
-- joining multiple tables

USE store;

SELECT
	o.order_id,
    o.order_date,
    c.first_name,
    c.last_name,
    os.name AS status
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id
JOIN order_statuses os
	ON o.status = os.order_status_id;

-- exercise

USE sql_invoicing;

SELECT 
	p.date,
    p.invoice_id,
    p.amount,
    c.name,
    pm.name
FROM payments p
JOIN clients c
	ON p.client_id = c.client_id
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id;

-- compound join conditions (composite primary keys)

SELECT *
FROM order_items oi
JOIN order_item_notes oin
	ON oi.order_id = oin.order_id
    AND oi.product_id = oin.product_id;


-- implicit join syntax

SELECT * 
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id;

-- (equivalent statement but not recommended)
SELECT *
FROM orders o, customers c	
WHERE o.customer_id = c.customer_id;


-- OUTER JOIN

SELECT 
	c.customer_id,
    c.first_name,
    o.order_id
FROM customers c
JOIN orders o
	ON c.customer_id = o.customer_id  -- we only get customers who already have an order
ORDER BY c.customer_id;

-- what if we want ALL customers? regardless of order status

SELECT 
	c.customer_id,
    c.first_name,
    o.order_id
FROM customers c   -- LEFT TABLE
LEFT JOIN orders o  
	ON c.customer_id = o.customer_id
ORDER BY c.customer_id;

SELECT 
	c.customer_id,
    c.first_name,
    o.order_id
FROM customers c   
RIGHT JOIN orders o   -- RIGHT TABLE  
	ON c.customer_id = o.customer_id
ORDER BY c.customer_id;


-- OUTER JOIN
SELECT 
	c.customer_id,
    c.first_name,
    o.order_id
FROM orders o   
RIGHT JOIN customers c  -- RIGHT TABLE  
	ON c.customer_id = o.customer_id
ORDER BY c.customer_id;

-- join products table with order items table
SELECT 
	p.product_id, 
    p.name, 
    oi.quantity
FROM products p
LEFT JOIN order_items oi  -- left join will grab all the products form the LEFT table (p)
	ON p.product_id = oi.product_id;


-- OUTER JOIN USING MULTIPLE TABLES

SELECT 
	c.customer_id,
    c.first_name,
    o.order_id,
    s.name AS shipper
FROM customers c
LEFT JOIN orders o  -- get all the customers regardless of whether they have an order
	ON c.customer_id = o.customer_id 
LEFT JOIN shippers s
	ON o.shipper_id = s.shipper_id
ORDER BY c.customer_id;

-- best practice, avoid right joins and use left joins only

SELECT 
	o.order_date,
    o.order_id,
    c.first_name AS customer,
    s.name AS shipper,
    os.name AS status
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id
LEFT JOIN shippers as s
	ON o.shipper_id = s.shipper_id
LEFT JOIN order_statuses os
	ON o.status = os.order_status_id
ORDER BY o.order_id;

-- self outer joins

USE sql_hr;

SELECT
	e.employee_id,
    e.first_name,
    m.first_name AS manager
FROM employees e
LEFT JOIN employees m
	ON e.reports_to = m.employee_id;
    
