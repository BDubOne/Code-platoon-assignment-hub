-- CREATE TABLE customers (
--     id SERIAL PRIMARY KEY,
--     street VARCHAR,
--     city VARCHAR,
--     zip VARCHAR,
--     country VARCHAR
-- );

-- \copy customers from './stage-1/data/customers.csv' CSV HEADER


-- CREATE TABLE stores (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR,
--     country VARCHAR
-- );

-- \copy stores from './stage-1/data/stores.csv' CSV HEADER

-- CREATE TABLE drivers (
--     id SERIAL PRIMARY KEY,
--     store_id INTEGER REFERENCES stores(id),
--     full_name VARCHAR
-- );

-- \copy drivers from './stage-1/data/drivers.csv' CSV HEADER

-- CREATE TABLE available_pizzas (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR,
--     cost INT
-- );

-- \copy available_pizzas from './stage-1/data/available_pizzas.csv' CSV HEADER

-- CREATE TABLE available_toppings (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR,
--     cost INT
-- );

-- \copy available_toppings from './stage-1/data/available_toppings.csv' CSV HEADER

-- CREATE TABLE orders (
--     order_id SERIAL PRIMARY KEY,
--     customer_id INTEGER REFERENCES customers(id),
--     date VARCHAR,
--     pizza_id INT REFERENCES available_pizzas(id),
--     store_id INT REFERENCES stores(id),
--     toppings TEXT
-- );
-- \copy orders from './stage-1/data/orders.csv' CSV HEADER

CREATE TABLE deliveries(
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    started_delivery TIME,
    completed_delivery TIME 
);
\copy deliveries from './stage-1/data/deliveries.csv' CSV HEADER