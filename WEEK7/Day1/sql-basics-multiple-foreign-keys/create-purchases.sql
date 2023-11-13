/* Create the purchases table */
DROP TABLE if EXISTS purchases;
CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    item_id INTEGER REFERENCES items(id),
    quantity INTEGER,
  
    customer_id INTEGER REFERENCES customers(id)
);