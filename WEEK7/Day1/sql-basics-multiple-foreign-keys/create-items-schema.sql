DROP TABLE if EXISTS items;
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    cost INT
)