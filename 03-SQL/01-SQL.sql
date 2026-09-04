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
(1,10,"adam","adam@gmail.com",198,200),
(2,19,"muna","muna@gmail.com",500,677),
(3,20,"shreya","shreya@gmail.com",222,122),
(4,19,"moo","moo@gmail.com",333,344);

SELECT id,name,age FROM user; -- selects the particular column
SELECT * FROM user; -- to show all
SELECT DISTINCT age FROM user; -- to show the distinct entries


CREATE TABLE posts(
	id INT PRIMARY KEY,
    content VARCHAR(100),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

