USE store;

SELECT * 
FROM customers
-- WHERE customer_id = 1 
ORDER BY first_name;




-- THE SELECT CLAUSE

SELECT first_name, last_name
FROM customers;

SELECT last_name, first_name, points
FROM customers;

SELECT 
	last_name, 
    first_name, 
    points, 
    points * 10 + 100
FROM customers;

SELECT 
	last_name, 
    first_name, 
    points, 
    (points * 10) + 100 AS 'discount_factor'  -- this is an alias using AS
FROM customers;

SELECT state
FROM customers;

SELECT DISTINCT state
FROM customers;

