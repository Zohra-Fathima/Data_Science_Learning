CREATE DATABASE college;

USE college;

CREATE TABLE student (
	rollno INT,
    name VARCHAR(30),
    age INT
);

INSERT INTO student
VALUES
(101, "adam", 12),
(102,"bob",14);

SELECT * FROM student;

SHOW DATABASES;

USE instagram;

CREATE TABLE user(
	age INT,
	CONSTRAINT CHECK(age >= 18),
	id INT ,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE,
    followers INT DEFAULT 0,
    following INT,
    PRIMARY KEY(id) -- makes a column unique and not null and used only for one
);

INSERT INTO user
(id,age,name,email,followers,following)
VALUES
(1,19,"adam","adam@gmail.com",198,200),
(2,18,"muna","muna@gmail.com",500,677),
(3,20,"shreya","shreya@gmail.com",222,122),
(4,21,"moo","moo@gmail.com",333,344);

-- update :-
UPDATE user
SET age =21
WHERE id =1;

UPDATE user
SET age =18
WHERE id =3;

UPDATE user
SET age =23
WHERE id =2;

-- delete:-
DELETE FROM user
WHERE age=18;



SELECT * FROM user;

SELECT id,name,age FROM user; -- selects the particular column
SELECT * FROM user; -- to show all
SELECT DISTINCT age FROM user; -- to show the distinct entries

-- where clause :- logical operators:
-- AND-to check for both conditions to be true
-- OR- to check for one of the conditions to be true
-- BETWEEN-selects for a given range
-- IN-matches any value in the list
-- NOT-to negate the given condition

-- WHERE CLAUSE:
SELECT * FROM user 
WHERE followers>=200; -- when we want to define a specific condition on our data use WHERE

SELECT name,age FROM user 
WHERE age>=18; -- we can also send specific column name

-- LIMIT CLAUSE:
SELECT name,age 
FROM user 
WHERE age>=18
LIMIT 2; -- can also be used without where clause sets a limit on the number of outputs(the condition gives 4 users ouput but i need only 2 users so i use limit)

-- ORDER BY CLAUSE:
SELECT name,age,followers
FROM user 
ORDER BY followers ASC;  
-- if we want to sort in descending use DESC. Note:by default the data is sorted into ascending order

-- Aggregate functions
SELECT max(followers)
from user;

SELECT min(followers)
from user;

SELECT avg(age)
from user;

SELECT sum(followers)
from user;

-- Group by:(generally we use group by with aggregate functions)
SELECT age,max(followers)
FROM user
GROUP BY age
HAVING max(followers) > 200;
-- where clause is for the table, having is for a group
-- grouping is necessary for having



CREATE TABLE posts(
	id INT PRIMARY KEY,
    content VARCHAR(100),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);


INSERT INTO posts
VALUES
(101,"zohra",1);

SELECT id,user_id FROM posts;
