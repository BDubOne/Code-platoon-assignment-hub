/* HOW MANY DRIVERS */

SELECT count(*)
from drivers;

-- - How many deliveries has each store made

SELECT count(deliveries.id), stores.name
FROM deliveries
JOIN orders ON orders.order_id=deliveries.order_id
JOIN stores ON stores.id=orders.store_id 
GROUP BY stores.id ;
-- - How many deliveries has each driver made
SELECT count(deliveries.id), drivers.full_name
FROM deliveries
JOIN orders ON orders.order_id=deliveries.order_id
JOIN stores ON stores.id=orders.store_id
JOIN drivers ON stores.id=drivers.store_id
GROUP BY drivers.id;

-- - Which driver did the shortest delivery

SELECT full_name, delivery_time
FROM (
    SELECT
        drivers.full_name,
        EXTRACT(EPOCH FROM deliveries.completed_delivery - deliveries.started_delivery) / 60 AS delivery_time,
        RANK() OVER (ORDER BY EXTRACT(EPOCH FROM deliveries.completed_delivery - deliveries.started_delivery)) AS delivery_rank
    FROM deliveries
    JOIN orders ON orders.order_id = deliveries.order_id
    JOIN stores ON stores.id = orders.store_id
    JOIN drivers ON stores.id = drivers.store_id
) ranked_drivers
-- ORDER BY delivery_rank ASC
-- LIMIT 1;
WHERE delivery_rank = 1;

-- - Which driver did the longest delivery

SELECT full_name, delivery_time
FROM (
    SELECT 
    drivers.full_name,
    EXTRACT (EPOCH FROM deliveries.completed_delivery - deliveries.started_delivery) / 60 AS delivery_time,
    RANK() OVER (ORDER BY EXTRACT(EPOCH FROM deliveries.completed_delivery - deliveries.started_delivery) DESC) AS delivery_rank
    FROM deliveries
    JOIN orders ON orders.order_id = deliveries.order_id
    JOIN stores ON stores.id = orders.store_id
    JOIN drivers ON stores.id = drivers.store_id
) ranked_drivers
WHERE delivery_rank = 1
