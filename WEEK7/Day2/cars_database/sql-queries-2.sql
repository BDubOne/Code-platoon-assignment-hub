SELECT count(appuser.account_id), userprofile.city
FROM appuser
JOIN userprofile on userprofile.account_id=appuser.account_id
GROUP BY userprofile.city
ORDER BY userprofile.city;

SELECT count(appuser.account_id), userprofile.city
FROM appuser
JOIN userprofile on userprofile.account_id=appuser.account_id
WHERE userprofile.city!='Chicago'
GROUP BY userprofile.city
ORDER BY userprofile.city;

SELECT count(advertisement_id), advertisement_date
FROM advertisement
GROUP BY advertisement_date
ORDER BY advertisement_date DESC;

SELECT count(advertisement_id), advertisement_date
FROM advertisement
WHERE advertisement_date < '2014-02-01'
GROUP BY advertisement_date
ORDER BY advertisement_date DESC;

-- select count(*) / 30
-- FROM advertisement;

SELECT
EXTRACT (MONTH from advertisement_date) AS month
COUNT(*) AS total_records
FROM advertisement
GROUP BY extract(MONTH FROM advertisement_date)
ORDER BY
month

select appuser.first_name, advertisement.advertisement_date
from appuser
join advertisement on advertisement.seller_account_id=appuser.account_id
where advertisement.advertisement_date BETWEEN '2014-06-01' AND '2014-06-30';

COPY (SELECT carmodel.make, carmodel.model, car.car_id, COUNT(advertisement.car_id)
FROM carmodel
JOIN car ON car.car_model_id=carmodel.car_model_id
JOIN advertisement ON car.car_id=advertisement.car_id
JOIN appuser ON appuser.account_id=advertisement.seller_account_id
WHERE appuser.first_name='Wilda' AND appuser.last_name='Giguere'
GROUP BY carmodel.make, carmodel.model, car.car_id) TO '~./#.csv' DELIMITER ',' CSV HEADER;


-- , COUNT(advertisement.car_id)