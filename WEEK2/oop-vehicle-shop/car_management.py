class CarManager:

    #Class variables :

    all_cars = {}

    total_cars = 0

    #car_id = total_cars

    def __init__(self, color="N/A", make="N/A", model="N/A", year="N/A", mileage="N/A", services=[]):
        CarManager.total_cars += 1
        self._id = CarManager.total_cars
        self._color = color
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services
        CarManager.all_cars[self._id] = self
    
    def __str__(self):
        return f"{self._id} | {self._color} | {self._make} | {self._model} | {self._year} | {self._mileage} | {self._services}"

    @property
    def get_id(self):
        return self._id
    
    @get_id.setter
    def set_id(self, new_id):
        if new_id.isnumeric():
            self._id = new_id
    
    @property
    def get_color(self):
        return self._color
    
    @get_color.setter
    def set_color(self, new_color):
        if isinstance(new_color, str):
            self._color = new_color

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
    def set_mileage(self, new_mileage):
        if isinstance(new_mileage, int):
            self._mileage = new_mileage
    
    @property
    def get_services(self):
        return self._services
    
    @get_services.setter
    def set_service(self, new_service):
        if isinstance(new_service, str):
            self._services.append(new_service)
    
    def add_service():
        CarManager.view_all_cars()
        car_serviced = int(input("choose the number of the car you want to service"))
        if car_serviced in CarManager.all_cars.keys():
            car_serviced = CarManager.all_cars[car_serviced]

        service_message = '''
------Welcome to our service center------
1. Change oil        |      2. Rotate Tires
3. Alignment         |      4. Tune-up'''
        print(service_message)
        service_center = {1:"change oil", 2:"rotate tires", 3: "get alignment", 4:"get tune-up"}

        choice = int(input("choose from the service menu"))

        if choice in service_center.keys():
            service_done = service_center[choice]
            car_serviced.set_service=service_done
    
    def view_car_details():
        CarManager.view_all_cars()
        car_to_view = int(input("which car do you want to look at?"))
        if car_to_view in CarManager.all_cars.keys():
            car_to_view = CarManager.all_cars[car_to_view]
        print(car_to_view)
    
    def update_mileage():
        CarManager.view_all_cars()
        car_to_update = int(input("which car do you want to look at?"))
        if car_to_update in CarManager.all_cars.keys():
            car_to_update = CarManager.all_cars[car_to_update]
        new_mileage = int(input("what is your current mileage?"))
        car_to_update.set_mileage=new_mileage
        



    def add_a_car():

        color = input("What color is your car?    ")
        make  = input("What is the make?    ")
        model = input("What is the model?"    )
        year = input("What is the year?    ")
        mileage = input("What is the mileage?"    )
        services = [input("what was the most recent service?")]

        CarManager(color, make, model, year, mileage, services)
        
    
    @staticmethod
    def view_all_cars():
        for index in CarManager.all_cars:
            print(CarManager.all_cars[index])
        
    
    @staticmethod
    def inventory_size():
        print(f"{CarManager.total_cars} on our lot!")
    #Begin Instance
    
    def main():
    
        welcome_message = '''
    -------Welcome to Our World-Famous Car Lot-------  
                
    1. Add a car           |        2. View all cars
    3. See inventory size  |        4. See car details 
    5. Service a car       |        6. Update Mileage
    7. quit
        ''' 
        while True:
            print(welcome_message)
            selection = int(input("what would you like to do?"))
            if isinstance(selection, int) and (1 <= selection <= 7):
                if selection == 1:
                    CarManager.add_a_car()
                elif selection == 2:
                    CarManager.view_all_cars()
                elif selection == 3:
                    CarManager.inventory_size()
                elif selection == 4:
                    CarManager.view_car_details()
                elif selection == 5:
                    CarManager.add_service()
                elif selection == 6:
                    CarManager.update_mileage()
                elif selection == 7:
                    break


    
    
        
    

            

       