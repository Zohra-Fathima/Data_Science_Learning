SELECT @@autocommit;

SET autocommit =0;

CREATE DATABASE prime;

USE prime;

CREATE TABLE accounts(
	id INT PRIMARY KEY auto_increment,
    name VARCHAR(10),
    balance DECIMAL(10,2)
);


INSERT INTO accounts (name,balance)
 VALUES
("adam",500.0),
("bob",300.00),
("charlie",1000.00);

SELECT * FROM accounts;

-- transactions

START TRANSACTION;

UPDATE accounts SET balance = balance + 1000 WHERE id = 1;
SAVEPOINT after_wallet_topup;

UPDATE accounts SET balance = balance + 501 WHERE id = 1;
-- error
ROLLBACK TO after_wallet_topup;
COMMIT;


-- JOINS:-
CREATE TABLE customers(
	customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO customers 
VALUES
(1,"alice","mumbai"),
(2,"bob","delhi"),
(3,"charlie","bengalure"),
(4,"david","mumbai");

CREATE TABLE orders(
	order_id INT PRIMARY KEY,
    customer_id INT,
    amount INT
);

INSERT INTO orders VALUES
(101,1,500),
(102,1,600),
(103,2,700),
(104,5,800);

SELECT * FROM customers;
SELECT * FROM orders;

-- INNER JOIN:
SELECT *
FROM customers c --  syntax:from tableA INNER JOIN to tableB
INNER JOIN orders o
ON c.customer_id = o.customer_id;

-- LEFT JOIN:
SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;

-- RIGHT JOIN:
SELECT *
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

-- OUTER JOIN
SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
UNION
SELECT *
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

-- CROSS JOIN:
SELECT*
FROM customers
CROSS JOIN orders;

-- SELF JOIN:
SELECT *
FROM customers as A
JOIN customers as B
on A.customer_id= B.customer_id;

-- LEFT EXCLUSIVE JOIN:
SELECT * 
FROM customers as A
LEFT JOIN orders as B
ON A.customer_id = B.customer_id
WHERE B.customer_id IS NULL;

-- RIGHT EXCLUSIVE JOIN:
SELECT * 
FROM customers as A
RIGHT JOIN orders as B
ON A.customer_id = B.customer_id
WHERE A.customer_id IS NULL; 

SELECT * FROM customers;
SELECT * FROM orders;

-- sub queries:-
SELECT * FROM orders
WHERE amount > (
	SELECT AVG(amount)
    FROM orders
);

-- sub queries inside(with) SELECT:
SELECT name,
	(
		SELECT COUNT(*)
		FROM orders o
		WHERE o.customer_id= c.customer_id
	)
    AS order_count
	FROM customers c;

-- sub queries inside(with) FROM:
SELECT
 summary.customer_id,
 summary.avg_amount
FROM 
	(
		SELECT
			customer_id,
			AVG(amount) as avg_amount
		FROM orders
		GROUP BY customer_id
	) AS summary;

