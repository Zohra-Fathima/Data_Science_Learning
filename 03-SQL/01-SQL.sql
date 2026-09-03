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
    email VARCHAR(50),
    followers INT DEFAULT 0,
    following INT,
    PRIMARY KEY(id) -- makes a column unique and not null and used only for one
);

CREATE TABLE posts(
	id INT PRIMARY KEY,
    content VARCHAR(100),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

