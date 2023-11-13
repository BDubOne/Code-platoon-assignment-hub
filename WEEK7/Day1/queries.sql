SELECT customers.email, purchases.item from customers
JOIN purchases on customers.id=purchases.customer_id
where customers.first_name='alice';
