USE store;

SELECT *
FROM products;

SELECT 
	name, 
    unit_price,
    (unit_price * 1.1) AS 'new_price'
FROM products;


-- WHERE
--  >  >=  <  <=  =  (!=  or <>)

SELECT *
FROM customers
WHERE points > 3000;

SELECT *
FROM customers
WHERE state = 'VA';  -- or 'va' or "VA"

SELECT * 
FROM customers 
WHERE state <> 'VA';

-- dates
SELECT *
FROM customers
WHERE birth_date > '1990-01-01';


-- EXERCISE
SELECT * 
FROM orders
WHERE order_date >= '2019-01-01';


SELECT *
FROM customers
WHERE birth_date > '1990-01-01' AND points > 1000;

SELECT *
FROM customers
WHERE birth_date > '1990-01-01' OR points > 1000;

SELECT *
FROM customers
WHERE birth_date > '1990-01-01' OR 
	(points > 1000 AND state = 'VA');
-- order of operators is important:  AND executed before OR 


SELECT *
FROM customers
WHERE NOT (birth_date > '1990-01-01' OR points > 1000);


-- EXERCISE

SELECT * 
FROM order_items
WHERE order_id = 6 AND (unit_price * quantity) > 30; 


