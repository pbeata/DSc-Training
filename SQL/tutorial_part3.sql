USE store;

SELECT *
FROM customers
WHERE state = 'VA' OR state = 'GA' OR state = 'FL';

-- we can do the same thing, but this time with the IN operator

SELECT *
FROM customers
WHERE state IN ('VA', 'FL', 'GA');

SELECT *
FROM customers
WHERE state NOT IN ('VA', 'FL', 'GA');

SELECT *
FROM products
WHERE quantity_in_stock IN (49, 38, 72);

-- BETWEEN

SELECT *
FROM customers
-- WHERE points >= 1000 AND points <= 3000;
WHERE points BETWEEN 1000 AND 3000;  -- range values are inclusive

SELECT *
FROM customers
WHERE birth_date BETWEEN '1990-01-01' AND '2000-01-01';

-- LIKE

SELECT *
FROM customers
-- WHERE last_name LIKE 'b%';  -- last name starts with B
-- WHERE last_name LIKE 'brush%';
-- WHERE last_name LIKE '%b%';   -- has a B anywhere in their last name
-- WHERE last_name LIKE '%y';  -- last names that end in y
WHERE last_name LIKE 'b______y';

SELECT *
FROM customers
WHERE address LIKE '%trail%' OR 
	  address LIKE '%avenue%';

SELECT *
FROM customers
WHERE phone LIKE '%9';

SELECT *
FROM customers
WHERE phone NOT LIKE '%9';

-- REGULAR EXPRESSIONS

SELECT *
FROM customers
-- WHERE last_name LIKE '%field%'
-- WHERE last_name REGEXP 'field';
-- WHERE last_name REGEXP '^field';  -- ^ start with field
-- WHERE last_name REGEXP 'field$';
-- WHERE last_name REGEXP '^field|mac|rose'; 
-- WHERE last_name REGEXP '[gim]e';
WHERE last_name REGEXP '[a-h]e';

-- ^ beginning
-- $ end
-- | logical or
-- [abcd]
-- [a-f] range of characters


-- get customers whose:

-- first names are ELKA or AMBUR
SELECT *
FROM customers
WHERE first_name REGEXP 'elka|ambur';

-- last names end with EY or ON
SELECT *
FROM customers
WHERE last_name REGEXP 'ey$|on$';

-- last names start with MY or contains SE
SELECT *
FROM customers
WHERE last_name REGEXP '^my|se';

-- last names contain B followed by R or U
SELECT *
FROM customers
-- WHERE last_name REGEXP 'b[ru]';
WHERE last_name REGEXP 'br|bu';


-- NULL VALUES

SELECT *
FROM customers
WHERE phone IS NULL;

SELECT *
FROM customers
WHERE phone IS NOT NULL;

SELECT *
FROM orders
WHERE shipped_date IS NULL OR shipper_id IS NULL;

-- sorting data in your SQL queries

SELECT first_name, last_name, 10 AS points
FROM customers
-- ORDER BY first_name;
-- ORDER BY first_name DESC;
ORDER BY state DESC, points;

-- EX

SELECT *, (quantity * unit_price) AS total_price
FROM order_items
WHERE order_id = 2
ORDER BY total_price DESC;

SELECT *
FROM customers
LIMIT 6, 3;  -- OFFSET goes first (6, so in this case, skip 6), and
-- (3) only gives the first 3 results

-- e.g.
-- page 1: 1 - 3
-- page 2: 4 - 6
-- page 3: 7 - 9


-- get top 3 loyal customers
SELECT *
FROM customers
-- WHERE ...
ORDER BY points DESC
LIMIT 3;
-- (this is a good example of how ORDER matters in your SQL queries)












