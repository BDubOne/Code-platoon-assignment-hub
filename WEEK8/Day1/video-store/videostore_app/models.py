from django.db import models

class Person(models.Model):
    first_name: models.CharField(max_length=100,null=False, blank=False)
    last_name: models.CharField(max_length=100, null=False, blank=False)
    middle_init: models.CharField(max_length=1, default=None)
    age: models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'
    
    @property
    def get_age(self):
        return self.age
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int):
            self.age = new_age


class Client(Person):
    account_type: models.CharField(max_length=20, default='Standard')
    email: models.EmailField(max_length=250, null=False, blank=False)
    active: models.BooleanField(default=False)

    def __str__(self):
        return f'name:{self.first_name} {self.last_name}\naccount-type: {self.account_type}\nemail: {self.email}\nactive:{self.active}\nage:{self.age} years old'

    @property 
    def get_account_type(self):
        return self.account_type
    @get_account_type.setter
    def set_account_type(self,new_account_type):
        self.account_type=new_account_type

