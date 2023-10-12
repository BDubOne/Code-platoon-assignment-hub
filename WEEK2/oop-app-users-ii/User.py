import re


class User:
    user_list = {}
    all_posts = []
    total_users = 0
    total_posts = 0
    def __init__(self, name, age, email, dl_number, address, favorite_food, favorite_band, posts=[]):
        User.total_users += 1
        self._id = User.total_users
        self._name = name
        self._age = age
        self._email = email
        self._dl_number = dl_number
        self._address = address
        self._favorite_food = favorite_food
        self._favorite_band = favorite_band
        self._posts = []
        User.user_list[self._id] = self
     
    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}\nEmail: {self._email}\nDL Number: {self._dl_number}\nAddress: {self._address}\nFavorite Food: {self._favorite_food}\nFavorite Band: {self._favorite_band}"
    
    @property
    def get_name(self):
        return self._name
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name

    @property
    def get_age(self):
        return self._age
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
    
    @property 
    def get_email(self):
        return self._email
    @get_email.setter
    def set_email(self, new_email):
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.match(pat,new_email):
            self._email = new_email

    
   
    @classmethod
    def create_post(cls):
        User.total_posts += 1
        post_id = User.total_posts
        title = input("What is the title of your post?  ")
        description = input("What do you have  to say?     ")
        post = {title: description, "Post": post_id}
        User.all_posts.append(post)
        return post
    
    @classmethod 
    def remove_post(cls):
        User.view_all_posts()
        print("which post do you want to remove?")
        choice = int(input("choose the correct index number"))
        User.all_posts.pop(choice)
        User.view_all_posts()
        

    
    def create_post(self):
        User.total_posts += 1
        post_id = User.total_posts
        title = input("What is the title of your post?  ")
        description = input("What do you have  to say?     ")
        post = {title: description, "Post": post_id}        
        self.posts.append(post)
        User.all_posts.append(post)
       
    
    def view_user_posts(self):
        for post in self.posts:
            print(post)

    @staticmethod
    def view_all_posts():
        for post in User.all_posts:
            print(post) 



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