class CarManager:

    #Class variables :

    all_cars = {}

    total_cars = 0

    #car_id = total_cars

    def __init__(self, make, model, year, mileage, services=[]):
        CarManager.total_cars += 1
        self._id = CarManager.total_cars
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services
        CarManager.all_cars[self] = self
    
    def __str__(self):
        return f"{self._id} | {self._make} | {self._model} | {self._year} | {self._mileage} | {self._services}"

    @property
    def get_id(self):
        return self._id
    
    @get_id.setter
    def set_id(self, new_id):
        if new_id.isnumeric():
            self._id = new_id

    @property
    def get_make(self):
        return self._make
    
    @get_make.setter
    def set_make(self, new_make):
        if isinstance(new_make, str):
            self._make = new_make

    @property
    def get_model(self):
        return self._model
    
    @get_model.setter
    def set_model(self, new_model):
        if isinstance(new_model, str):
            self._model = new_model

    @property
    def get_year(self):
        return self._year
    
    @get_year.setter
    def set_year(self, new_year):
        if isinstance(new_year, int):
            self._model = new_year

    @property
    def get_mileage(self):
        return self._mileage
    
    @get_mileage.setter
    def define_mileage(self, new_mileage):
        if isinstance(new_mileage, int):
            self._mileage = new_mileage
    
    @property
    def get_services(self):
        return self._services
    
    @get_services.setter
    def add_service(self, new_service):
        if isinstance(new_service, str):
            self.services.append(new_service)
    
    def view_all_cars():
        for index in CarManager.all_cars:
            print(CarManager.all_cars[index])

    

            

       