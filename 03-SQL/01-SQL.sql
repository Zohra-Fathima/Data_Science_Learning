CREATE DATABASE college;

CREATE DATABASE IF NOT EXISTS instagram;

USE instagram;

CREATE TABLE user(
	id INT ,
    age INT,
    name VARCHAR (10) NOT NULL,
    email INT UNIQUE,
    followers INT DEFAULT 0,
    following INT
    CONSTRAINT CHECK(age>=13)
);