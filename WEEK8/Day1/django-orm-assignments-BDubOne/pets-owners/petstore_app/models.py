from django.db import models

class Owner(models.Model):
    name=models.CharField(null=False,blank=False)
    age=models.PositiveIntegerField(default=29)
    number_of_pets=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} has {self.number_of_pets} pets'
    
    @property
    def get_age(self):
        return self.age
    @get_age.setter
    def set_age(self, new_age):
        self.age=new_age
    
    @property
    def get_number_of_pets(self):
        return self.number_of_pets
    @get_number_of_pets.setter
    def set_number_of_pets(self, new_number_of_pets):
        self.number_of_pets = new_number_of_pets

class Animal(models.Model):
    name=models.CharField(max_length=100, default="X")
    age=models.PositiveIntegerField(null=True, blank=True)
    vaccinated=models.BooleanField(default=False)
    description=models.TextField(default="unknown")

    def __str__(self):
        return f"name: {self.name} | description: {self.description} | vacinnated: {self.vaccinated} "

    @property
    def get_age(self):
        return self.age
    @get_age.setter
    def set_age(self, new_age):
        self.age=new_age
    
    @property
    def get_vaccinated(self):
        return self.vaccinated
    @get_vaccinated.setter
    def set_vacinnated(self, new_vaccinated):
        if isinstance(new_vaccinated, bool):
            self.vaccinated=new_vaccinated
    
    @property
    def get_description(self):
        return self.description
    @get_description.setter
    def set_description(self, new_description):
        self.description=new_description

    @property
    def get_name(self):
        return self.name
    @get_name.setter
    def set_name(self, new_name):
        self.name=new_name
    
class Cat(Animal):
    breed=models.CharField(default='unknown')

    def __str__(self):
        return f"Cat \nname: {self.name} breed: {self.breed}| description: {self.description} | vacinnated: {self.vaccinated} "

    @property 
    def get_breed(self):
        return self.breed
    @get_breed.setter
    def set_breed(self, new_breed):
        self.breed=new_breed

    
    

class Bird(Animal):
    species=models.CharField(default='unknown')

    def __str__(self):
        return f"Bird \nname: {self.name} species: {self.species}| description:  {self.description} | vacinnated: {self.vaccinated} "

    @property 
    def get_species(self):
        return self.species
    @get_species.setter
    def set_species(self, new_species):
        self.species=new_species

class Dog(Animal):
    breed=models.CharField(default='unknown')    

    def __str__(self):
        return f"Dog \nname: {self.name} breed: {self.breed}| description:  {self.description} | vacinnated: {self.vaccinated} "   

    @property 
    def get_breed(self):
        return self.breed
    @get_breed.setter
    def set_breed(self, new_breed):
        self.breed=new_breed

class ExoticAnimal(Animal):
    region_of_origin = models.CharField(max_length=250, default="earth")
    type_of_animal=models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Exotic \nname: {self.name} type: {self.breed}| origin: {self.region_of_origin} description:  {self.description} | vacinnated: {self.vaccinated}"
    
    @property
    def get_region_of_origin(self):
        return self.region_of_origin
    @get_region_of_origin.setter
    def set_region_of_origin(self, new_region_of_origin):
        self.region_of_origin=new_region_of_origin

       


    

   

