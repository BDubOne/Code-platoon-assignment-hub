SELECT count(*) FROM appuser;

SELECT count(*) 
FROM appuser
where first_name like 'R%';

SELECT first_name, last_name 
FROM appuser
ORDER BY last_name
LIMIT 5;

SELECT AVG(mileage)
FROM car;

SELECT AVG(mileage)
FROM car
where number_of_owners >= 3;

SELECT AVG(mileage)
FROM car
WHERE number_of_owners >= 3 AND manufacture_year >2008;

SELECT MAX(char_length(model))
FROM carmodel;

SELECT count(*)
FROM appuser
JOIN userprofile ON appuser.account_id=userprofile.account_id
WHERE userprofile.city LIKE 'Chicago%';

SELECT count(*)
FROM appuser
JOIN userprofile ON appuser.account_id=userprofile.account_id
WHERE userprofile.city LIKE '%Park%'


