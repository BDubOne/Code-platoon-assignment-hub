DROP TABLE IF EXISTS information CASCADE;
CREATE TABLE information(
    id SERIAL PRIMARY KEY,
    street_address VARCHAR,
    city VARCHAR,
    us_state VARCHAR,
    email VARCHAR,
    phone VARCHAR
);

DROP TABLE IF EXISTS accounts CASCADE;
CREATE TABLE accounts(
    id SERIAL PRIMARY KEY,
    type VARCHAR,
    info_id INT REFERENCES information(id),
    acct_number INTEGER
);


DROP TABLE IF EXISTS owners CASCADE;
CREATE TABLE owners(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    salary INT,
    inc_date DATE,
    info_id INT REFERENCES information(id),
    primary_acct_id INTEGER REFERENCES accounts(id)
);

DROP TABLE IF EXISTS stores CASCADE;
CREATE TABLE stores(
    id SERIAL PRIMARY KEY, 
    est_date DATE,
    owner_id INT,
    info_id INT REFERENCES information(id),
    primary_acct_id INTEGER REFERENCES accounts(id)
);

DROP TABLE IF EXISTS employees CASCADE;
CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    title VARCHAR,
    pay_rate INT,
    start_date DATE,
    info_id INT REFERENCES information(id),
    primary_acct_id INTEGER REFERENCES accounts(id),
    store_id INTEGER REFERENCES stores(id)
);

DROP TABLE IF EXISTS items CASCADE;
CREATE TABLE items(
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    quantity INTEGER,
    cost INTEGER,
    store_id INTEGER REFERENCES stores(id)
);


DROP TABLE IF EXISTS sales;
CREATE TABLE sales(
    id SERIAL PRIMARY KEY,
    time TIME,
    date DATE,
    price INTEGER,
    quantity INTEGER,
    item_id INTEGER REFERENCES items(id),
    employee_id INTEGER REFERENCES employees(id),
    store_id INTEGER REFERENCES stores(id)
);

DROP TABLE IF EXISTS timesheets;
CREATE TABLE timesheets(
    id SERIAL PRIMARY KEY,
    time_in TIME,
    time_out TIME,
    date DATE,
    employee_id INTEGER REFERENCES employees(id),
    store_id INTEGER REFERENCES stores(id)
);











