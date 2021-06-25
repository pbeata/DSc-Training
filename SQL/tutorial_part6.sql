
INSERT INTO customers (
	first_name,
    last_name,
    birth_date,
    address,
    city,
    state)
VALUES (
	-- DEFAULT, -- DEFAULT for auto-incrementing values
	'John', 
	'Smith', 
	'1990-01-01',
    -- NULL,
    '123 Main St',
    'San Francisco',
	'CA')
    -- DEFAULT)
;

INSERT INTO shippers (name)
VALUES ('Shipper1'),
	   ('Shipper2'),
       ('Shipper3');
       
SELECT * FROM shippers;

-- insert three rows into the products table

INSERT INTO products (name, quantity_in_stock, unit_price)
VALUES ('Taco', 1, 2.99),
	   ('Hot Dog', 4, 1.99),
       ('Water', 2, 0.99);

-- hierarchical data

INSERT INTO orders (customer_id, order_date, status)
VALUES (1, '2019-01-02', 1);

-- MySQL built-in functions

-- SELECT LAST_INSERT_ID()

-- copy of table

USE sql_store;

CREATE TABLE orders_archived AS
SELECT * FROM orders;

INSERT INTO orders_archived
SELECT * 
FROM orders
WHERE order_date < '2019-01-01';


CREATE TABLE invoices_archived AS
SELECT 
	i.invoice_id,
    i.number,
    c.name AS client,
    i.invoice_total,
    i.payment_total,
    i.invoice_date,
    i.payment_date,
    i.due_date
FROM invoices i
JOIN clients c
	USING (client_id)
WHERE i.payment_date IS NOT NULL; 

-- updating a single row of data

UPDATE invoices
SET payment_total = 10, payment_date = '2019-01-02'
WHERE invoice_id = 1;

UPDATE invoices
SET payment_total = DEFAULT, payment_date = NULL
WHERE invoice_id = 2;

UPDATE invoices
SET 
	payment_total = invoice_total * 0.5, 
    payment_date = due_date
WHERE invoice_id = 3;

-- update multiple records 

UPDATE invoices
SET 
	payment_total = invoice_total * 0.5, 
    payment_date = due_date
WHERE client_id = 3;

UPDATE invoices
SET 
	payment_total = invoice_total * 0.5, 
    payment_date = due_date
WHERE client_id IN (4,5);

USE sql_store;

SELECT *
FROM customers
WHERE birth_date < '1990-01-01';

UPDATE customers
SET points = points + 50
WHERE birth_date < '1990-01-01';

SELECT *
FROM customers
WHERE birth_date < '1990-01-01';

USE sql_invoicing;

UPDATE invoices
SET 
	payment_total = invoice_total * 0.5, 
    payment_date = due_date
WHERE client_id = (
		SELECT client_id
		FROM clients
		WHERE name = 'MyWorks')
;

SELECT client_id
FROM clients
WHERE state IN ('CA', 'NY');


UPDATE invoices
SET 
	payment_total = invoice_total * 0.5, 
    payment_date = due_date
WHERE client_id IN (
		SELECT client_id
		FROM clients
		WHERE state IN ('CA', 'NY') 
        )
;

SELECT *
FROM invoices 
WHERE payment_date IS NULL;

UPDATE invoices 
SET payment_total = invoice_total
WHERE payment_date <= due_date;

-- sub query with update statement
UPDATE orders
SET comments = 'Gold Customer'
WHERE customer_id IN (
		SELECT customer_id
		FROM customers
		WHERE points > 3000
		);
        
-- how to delete records from a table

USE sql_invoicing;

-- USE CAUTION
DELETE FROM invoices
WHERE invoice_id = 1;

DELETE FROM invoices 
WHERE client_id = (
	SELECT *
    FROM clients
    WHERE name = 'Myworks'
);


-- restore databases to their original state (before the modifications)


