-- create user user_0d_1

-- create
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- grant
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
