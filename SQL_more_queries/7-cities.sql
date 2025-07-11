-- create db hbtn_0d_usa and table cities

-- create db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
