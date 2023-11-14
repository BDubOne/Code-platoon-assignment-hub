select car.car_id, car.registration_number, carmodel.car_model_id,
carmodel.make, carmodel.model from car
JOIN CarModel
ON car.car_id=carmodel.car_model_id
-- WHERE carmodel.make like '%Mercede%';
-- WHERE carmodel.model like 'A%';
WHERE carmodel.make IN ('Mercedes Benz', 'Ford');

-- cars=# SELECT * from advertisement where advertisement_date BETWEEN '2014-01-01' AND '2014-01-31' ORDER BY advertisement_date;



SELECT COUNT(*) AS user_count FROM appuser;

-- SELECT car.car_id, car.registration_number, car.number_of_doors, car.mileage, car.car_model_id, carmodel.car_model_id, carmodel.make, carmodel.model
-- FROM car 
-- JOIN carmodel 
-- ON car.car_model_id=carmodel.car_model_id
-- where number_of_doors=3;

SELECT  CONCAT(AppUser.first_name, ' ', AppUser.last_name) as full_name, COUNT(Advertisement.car_id) as number_of_ads,CarModel.make, CarModel.model, Car.number_of_owners, Car.manufacture_year, Car.mileage
FROM AppUser
JOIN Advertisement ON AppUser.account_id=Advertisement.seller_account_id
JOIN Car ON Advertisement.car_id=Car.car_id
JOIN CarModel ON Car.car_model_id=CarModel.car_model_id
WHERE Car.manufacture_year > 2013 AND Car.mileage < 100000 AND CarModel.make != 'BMW' AND CarModel.make != 'Peugeot' AND CarModel.make != 'Opel'
GROUP BY full_name, CarModel.make, CarModel.model, Car.manufacture_year, Car.mileage,Car.number_of_owners;

SELECT Appuser.first_name, appuser.last_name, appuser.email, userprofile.city, advertisement.advertisement_date, car.registration_number,
carmodel.make, carmodel.model
FROM appuser 
JOIN userprofile ON appuser.account_id=userprofile.account_id
Join advertisement On appuser.account_id=advertisement.seller_account_id
join car on advertisement.car_id=car.car_id
join carmodel on carmodel.car_model_id=car.car_model_id
WHERE appuser.first_name='Elly';