\c postgres

DROP DATABASE IF EXISTS grocery_store;

CREATE DATABASE grocery_store;

\c grocery_store

create table stores(
    id SERIAL PRIMARY KEY
);

insert into stores values(default);

create table customers(
    id serial primary key,
    store_id INT REFERENCES stores(id),
    email VARCHAR NOT NULL UNIQUE
);

INSERT INTO customers(store_id, email) VALUES
(1, 'alice@gmail.com'),
(1, 'bob@gmail.com');

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    store_id INTEGER REFERENCES stores(id),
    name VARCHAR,
    price numeric
);

INSERT INTO PRODUCTS(store_id, name, price) VALUES 
(1,'milk', 5),
(1,'milk', 3);
-- customers 

CREATE TABLE customer_products (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER
);

INSERT INTO customer_products(customer_id, product_id, quantity) VALUES
(1,1,2),
(1,1,2),
(2,1,2),
(2,1,2),
(2,1,2),
(1,1,2),
(1,1,2);
--customer-profiles

-- discounts/memberships

--items

--store

--sales

