--Which customer made the most purchases

SELECT customers.email, count(product_id ), sum(quantity) as products_purchased
FROM customer_products
JOIN customers on customers.id=customer_products.customer_id
GROUP BY customers.email
ORDER by products_purchased DESC
LIMIT 1;



--what is the total cost of each order

SELECT products.name, products.price * customer_products.quantity as total_cost
from customer_products
join products on products.id=customer_products.product_id;
--what is the best-selling product

--total revenue of the store

