-- /* If I want to get the employee id, employee name, total sales and total time, this is a good query*/

SELECT 
    stores.id,
    employees.first_name,
    SUM(sales.price*sales.quantity) AS total_sales,
    EXTRACT(EPOCH FROM SUM
    (timesheets.time_out - timesheets.time_in))
     / 3600 
     AS hours_worked
FROM stores

INNER JOIN employees ON stores.id = employees.store_id
LEFT JOIN sales ON employees.id = sales.employee_id
LEFT JOIN timesheets ON employees.id = timesheets.employee_id
GROUP BY stores.id, employees.first_name
ORDER BY stores.id, employees.first_name;


/* Here I get the first and last name of each owner along with the amount of stores owned, the revenue, and the profit */

SELECT owners.first_name,
owners.last_name,
COUNT(DISTINCT stores.id) AS total_stores,
SUM(sales.price * sales.quantity) AS total_revenue,
SUM(sales.price * sales.quantity) - SUM(items.cost*sales.quantity) AS total_profits
FROM owners
LEFT JOIN stores ON owners.id = stores.owner_id
LEFT JOIN sales ON stores.id=sales.store_id
LEFT JOIN items ON sales.item_id = items.id
GROUP BY owners.first_name, owners.last_name 
ORDER BY owners.first_name, owners.last_name ;

