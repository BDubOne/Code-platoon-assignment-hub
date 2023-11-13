-- /* If I want to get the employee id, employee name, total sales and total time, this is a good query*/

SELECT 
    s.id AS store_id,
    e.first_name AS employee_first_name,
    SUM(sales.price*sales.quantity) AS total_sales,
    EXTRACT(EPOCH FROM SUM
    (employees.time_out - employees.time_in))
     / 3600 
     AS hours_worked
FROM stores AS s

INNER JOIN employees AS e ON s.id = e.store_id
LEFT JOIN sales ON e.id = sales.employee_id
LEFT JOIN timesheets AS employees ON e.id = employees.employee_id
GROUP BY s.id, e.first_name
ORDER BY s.id, e.first_name;


/* Here I get the first and last name of each owner along with the amount of stores owned, the revenue, and the profit */

SELECT o.first_name AS owner_first_name,
o.last_name AS owner_last_name,
COUNT(DISTINCT s.id) AS total_stores,
SUM(sales.price * sales.quantity) AS total_revenue,
SUM(sales.price * sales.quantity) - SUM(items.cost*sales.quantity) AS total_profits
FROM owners AS o
LEFT JOIN stores AS S ON o.id = s.owner_id
LEFT JOIN sales ON s.id=sales.store_id
LEFT JOIN items ON sales.item_id = items.id
GROUP BY o.first_name, o.last_name 
ORDER BY o.first_name, o.last_name;

