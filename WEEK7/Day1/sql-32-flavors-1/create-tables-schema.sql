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

DROP TABLE IF EXISTS flavors CASCADE;
CREATE TABLE flavors(
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    cost INT,
    quantity INT,
    vegan BOOLEAN
);

DROP TABLE IF EXISTS cones CASCADE;
CREATE TABLE cones(
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    cost INT,
    quantity INT,
    gf BOOLEAN

);

DROP TABLE IF EXISTS materials CASCADE;
CREATE TABLE materials(
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    cost INT,
    quantity INT

);

DROP TABLE IF EXISTS products CASCADE;
CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    flavor_id INTEGER REFERENCES flavors(id),
    cone_id INTEGER REFERENCES cones(id),
    material_id INTEGER REFERENCES materials(id),
    quantity INTEGER,
    cost INTEGER,
    time_made TIMESTAMPTZ,
    store_id INTEGER REFERENCES stores(id)
);


DROP TABLE IF EXISTS sales;
CREATE TABLE sales(
    id SERIAL PRIMARY KEY,
    time TIME,
    date DATE,
    price INTEGER,
    quantity INTEGER,
    product_id INTEGER REFERENCES products(id),
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











