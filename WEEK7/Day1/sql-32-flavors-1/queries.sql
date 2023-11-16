-- /* If I want to get the employee id, employee name, total sales and total time, this is a good query*/
SELECT employees.id, employees.first_name, count(sales.id) as total_sales,
sum(EXTRACT(EPOCH FROM (timesheets.time_out - timesheets.time_in))) / 36000 as total_time_worked
FROM employees
JOIN sales ON sales.employee_id=employees.id
JOIN timesheets ON timesheets.employee_id=employees.id
GROUP BY employees.id,employees.first_name, timesheets.store_id
ORDER BY employees.id, timesheets.store_id;


SELECT 
    employees.id,
    employees.first_name,
    count(sales.id) as total_sales,
    sum(EXTRACT(EPOCH FROM (timesheets.time_out - timesheets.time_in))) / 36000 as total_hours_worked
FROM employees
JOIN sales ON sales.employee_id = employees.id
JOIN timesheets ON timesheets.employee_id = employees.id
GROUP BY employees.id, employees.first_name
ORDER BY employees.id;

/* Here I get the first and last name of each owner along with the amount of stores owned, the revenue, and the profit */


