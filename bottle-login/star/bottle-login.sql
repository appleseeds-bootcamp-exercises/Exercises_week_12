CREATE DATABASE bottle_login;
use bottle_login;
CREATE TABLE users (
    name VARCHAR(30) UNIQUE,
    hashed_password VARCHAR(50),
    session_id VARCHAR(50),
    last_login_attempt TIMESTAMP
);
INSERT INTO users VALUES ('sapir', 'ABC', 'eee');