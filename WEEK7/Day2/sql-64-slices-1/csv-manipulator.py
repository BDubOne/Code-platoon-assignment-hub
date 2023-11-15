import csv
import sqlite3
import psycopg2

# Replace 'db' with the name of your PostgreSQL database and 'username' with your PostgreSQL username
conn = psycopg2.connect(database='64-slices', user='your_username', password='your_password', host='your_host', port='your_port')


def parse_toppings(toppings_str):
    if toppings_str.strip():
        return [int(t) for t in toppings_str.strip('[]').split(',')]
    else: 
        return []

input_file = './stage-1/data/orders.csv'
conn = sqlite3.connect(`'64-slices.db'`)
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS orders (
               order_id SERIAL PRIMARY KEY,
               customer_id INTEGER REFERENCES customers(id),
               date TEXT,
               pizza_id INTEGER REFERENCES available_pizzas(id),
               store_id INTEGER REFERENCES stores(id)
               )
               ''')

# cursor.execute('''
#                CREATE TABLE IF NOT EXISTS available_toppings (
#                id SERIAL PRIMARY KEY,
#                name VARCHAR,
#                cost_per_pizza INTEGER               
#                )
#                ''')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS order_toppings(
               id SERIAL PRIMARY KEY,
               order_id INTEGER REFERENCES orders(order_id),
               topping_id INTEGER REFERENCES available_toppings(id)

                )
               ''')

output_file_orders='orders-updated.csv'
output_file_order_toppings='order_toppings.csv'
orders=[]
order_toppings=[]

with open(input_file, 'r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        order_id= row['order_id']
        customer_id = row['customer_id']
        date = row['date']
        pizza_id = row['pizza_id']
        store_id = row['store_id']
        toppings = parse_toppings(row['toppings'])

        cursor.execute('''
                   INSERT INTO orders (order_id, customer_id, date, pizza_id, store_id)
                   VALUES(?,?,?,?,?)
                   ''', (order_id, customer_id, date, pizza_id, store_id))
    
    

        for topping_id in toppings:
            cursor.execute('INSERT INTO order_toppings (order_id, topping_id) VALUES(?, ?)', (order_id, topping_id))

    
conn.commit()
conn.close()

print('data inserted into 64-slices')