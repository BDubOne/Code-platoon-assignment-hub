user_list = []
class User:
    def __init__(self, name, age, email, dl_number, address, favorite_food, favorite_band):
        self._name = name
        self._age = age
        self._email = email
        self._dl_number = dl_number
        self._address = address
        self._favorite_food = favorite_food
        self._favorite_band = favorite_band
     
    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}\nEmail: {self._email}\nDL Number: {self._dl_number}\nAddress: {self._address}\nFavorite Food: {self._favorite_food}\nFavorite Band: {self._favorite_band}"
    
    def get_name(self):
        return self._name
    



bryan = User("Bryan", 37, "bryan.t.bartell@gmail.com", 37373737, "321 Fake St.", "burritos", "Red Hot Chili Peppers")

annie = User("Annie", 48, "oneclassicom@gmail.com", 37373737, "321 Fake St.", "Prisoner's Food", "Nine Inch Nails")

unity = User("Unity", 17, "email@email.com", 37373737, "321 Fake St.", "Mashed Potatoes", "Metallica")

max = User("Maximus", 15, "email@email.com", 37373737, "321 Fake St.", "Oreo Milkshake", "Jojo's Bizarre Adventure Theme 1")

eko = User("Ekstasis", 15, "email@email.com", 37373737, "321 Fake St.", "Spaghetti", "CCR")

frank = User("Frank", 15, "email@email.com", 37373737, "321 Fake St.", "Fried Chicken", "CCR")

derek = User("Derek", 15, "email@email.com", 37373737, "321 Fake St.", "Fried Chicken", "CCR")

anna = User("Anna", 15, "email@email.com", 37373737, "321 Fake St.", "Chipotle", "CCR")

matt = User("Matt", 15, "email@email.com", 37373737, "321 Fake St.", "Chipotle", "CCR")

dakota = User("Dakota", 15, "email@email.com", 37373737, "321 Fake St.", "Chipotle", "CCR")


print(matt)

