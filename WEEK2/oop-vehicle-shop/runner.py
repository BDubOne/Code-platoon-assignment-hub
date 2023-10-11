from car_management import CarManager


honda = CarManager("grey","honda", "Civic", 1999, 350000, ["oil change", "tire rotation"])

chevy = CarManager("red","Chevy", "Camero", 1972, 50000, ["all the oil changes", "new head gaskets"])


CarManager.view_all_cars()

CarManager.main()
