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

select count(*) / 30
FROM advertisement;

select appuser.first_name
from appuser
join advertisement on advertisement.seller_account_id=appuser.account_id
where advertisement.advertisement_date BETWEEN '2014-06-01' AND '2014-06-30';

SELECT carmodel.make
FROM carmodel
JOIN car ON car.car_id=carmodel.car_model_id
JOIN advertisement ON car.car_id=advertisement.car_id
JOIN appuser ON appuser.account_id=advertisement.seller_account_id
WHERE appuser.first_name='Wilda' AND appuser.last_name='Giguere';


