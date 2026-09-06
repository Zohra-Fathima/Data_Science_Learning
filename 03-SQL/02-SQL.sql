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

-- LEFT EXCLUSIVE JOIN:(we want that data of A which is not common with B)
SELECT * 
FROM customers as A
LEFT JOIN orders as B
ON A.customer_id = B.customer_id
WHERE B.customer_id IS NULL;

-- RIGHT EXCLUSIVE JOIN:(we want that data of B which is not common with A)
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

#VIEW:-
CREATE VIEW view1 AS
SELECT customer_id, name FROM customers;

SELECT * FROM view1 WHERE name = "bob";

CREATE VIEW view2 AS
SELECT c.customer_id,c.name,o.order_id
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

SELECT * FROM view2;


-- INDEX:-
CREATE TABLE accounts(
	account_id INT PRIMARY KEY,
    name VARCHAR(10),
    balance DECIMAL(10,2),
    branch VARCHAR(20)
);

INSERT INTO accounts
 VALUES
(1,"adam",500.0,"mumbai"),
(2,"bob",300.00,"delhi"),
(3,"charlie",700.00,"bangalore"),
(4,"david",1000.00,"noida");

SELECT * FROM accounts;

-- single column indexing
CREATE INDEX idx_branch ON accounts(branch); 
SHOW INDEX FROM accounts; -- to see index

CREATE INDEX idx2 ON accounts(branch,balance); 

--  stored procedures:-CREATE INDEX idx_branch ON accounts(branch); 
-- creating a procedure:-
DELIMITER $$
CREATE PROCEDURE check_balance(IN acc_id INT)
BEGIN
	SELECT balance
    FROM accounts
    WHERE account_id=acc_id;
END $$

DELIMITER ;

CALL check_balance(1);  -- calling our prodecure