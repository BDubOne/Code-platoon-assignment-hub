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
CREATE TABLE owners (
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
    primary_acct_id INTEGER REFERENCES accounts(id) 
);

DROP TABLE IF EXISTS managers CASCADE;
CREATE TABLE managers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    employee_id INT REFERENCES employees(id),
    store_id INTEGER REFERENCES stores(id)
);



DROP TABLE IF EXISTS flavors CASCADE;
CREATE TABLE flavors(
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    cost INT,
    box_quantity INT,
    dairy_free BOOLEAN
);

DROP TABLE IF EXISTS cones CASCADE;
CREATE TABLE cones(
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    cost INT,
    box_quantity INT,
    gf BOOLEAN

);

DROP TABLE IF EXISTS materials CASCADE;
DROP TABLE IF EXISTS inventory CASCADE;
CREATE TABLE inventory(
    id SERIAL PRIMARY KEY,
    cone_id INTEGER REFERENCES cones(id),
    flavor_id INTEGER REFERENCES flavors(id),
    other_costs INT,
    UNIQUE (cone_id, flavor_id)
);

DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS sales_inventory CASCADE;
CREATE TABLE sales_inventory(
    id SERIAL PRIMARY KEY,
    inventory_id INTEGER REFERENCES inventory(id),
    time_made TIMESTAMPTZ,
    store_id INTEGER REFERENCES stores(id),
    UNIQUE (store_id, time_made)

);


DROP TABLE IF EXISTS sales CASCADE;
CREATE TABLE sales(
    id SERIAL PRIMARY KEY,
    time TIMESTAMPTZ,
    price INTEGER,
    quantity INTEGER,
    sales_inventory_id INTEGER REFERENCES sales_inventory(id),
    employee_id INTEGER REFERENCES employees(id)
);

DROP TABLE IF EXISTS timesheets;
CREATE TABLE timesheets(
    id SERIAL PRIMARY KEY,
    time_in TIMESTAMPTZ,
    time_out TIMESTAMPTZ,
    employee_id INTEGER REFERENCES employees(id),
    store_id INTEGER REFERENCES stores(id),
    UNIQUE (time_in, employee_id, store_id),
    UNIQUE (time_out, employee_id, store_id)
);

DROP TABLE IF EXISTS customers CASCADE;
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    acct_id INTEGER REFERENCES accounts(id),
    info_id INTEGER REFERENCES information(id)
);

DROP TABLE IF EXISTS customer_sales CASCADE;
CREATE TABLE customer_sales (
id SERIAL PRIMARY KEY,
customer_id INTEGER REFERENCES customers(id),
sale_id INTEGER REFERENCES sales(id),
UNIQUE (customer_id, sale_id)

);

DROP TABLE IF EXISTS customer_prizes;
CREATE TABLE customer_prizes (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    customer_sales_id INTEGER REFERENCES customer_sales(id),
    UNIQUE (customer_id, customer_sales_id)
);











