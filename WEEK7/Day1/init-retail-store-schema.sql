CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    email VARCHAR NOT NULL
);

/*
Create Purchases Table -- references Cutomers table 

*/

CREATE TABLE purchases(
    id SERIAL PRIMARY KEY,
    item VARCHAR,
    quantity INTEGER,
    cost INTEGER,
    customer_id INTEGER REFERENCES customers(id)
)