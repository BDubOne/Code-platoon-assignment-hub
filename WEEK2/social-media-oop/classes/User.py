import re


class User:
    total_posts = 0
    user_list = []
    all_posts = []
    total_users = 0
    def __init__(self, name, age=99, occupation="Life", email="N/A", phone="N/A", hobby="this", inspiration="everything", posts=[]):
        User.total_users += 1
        self._id = User.total_users
        self._name = name
        self._age = age
        self._occupation = occupation
        self._email = email
        self._phone = phone
        self._hobby = hobby
        self._inspiration = inspiration
        self.posts = posts

    def __repr__(self):
        return f"{self._id}: {self._name}: {self._email}. Inspired by {self._inspiration}"
    
    @property
    def get_name(self):
        return self._name
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name.title()
    
    @property
    def get_age(self):
        return self._age
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and 13 <= new_age < 151:
            self._age = new_age

    @property
    def get_occupation(self):
        return self._occupation
    @get_occupation.setter
    def set_occupation(self, new_occupation):
        if isinstance(new_occupation, str):
            self._occupation = new_occupation

    @property
    def get_email(self):
        return self._email
    @get_email.setter
    def set_email(self, new_email):
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.match(pat, new_email):
            self._email = new_email

    @property
    def get_phone(self):
        return self._phone
    @get_phone.setter
    def set_phone(self, new_phone): # Perhaps want to set regex perametrs. Or do this in a separate function that intakes user-input for a phone-number and accounts for/corrects error
        self._phone = str(new_phone)

    @property
    def get_hobby(self):
        return self._hobby
    @get_hobby.setter
    def set_hobby(self, new_hobby):
        if isinstance(new_hobby, str):
            self._hobby = new_hobby  #Perhaps want to later make this a list to append
    
    @property
    def get_inspiration(self):
        return self._inspiration
    @get_inspiration.setter
    def set_inspiration(self, new_inspiration):
        if isinstance(new_inspiration, str):
            self._inspiration = new_inspiration




   
    def create_a_post(self):
        post_title = input("What is your post title?")
        post_content = input("What do you have to say?")
        User.total_posts += 1
        this_post = [User.total_posts,{post_title: post_content}]
        User.all_posts.append(this_post)
        self.posts.append(this_post)

    @classmethod
    def admin_post(cls):
        post_title = input("Give the post a title")
        post_content = input("What is the message?")
        User.total_posts += 1
        this_post = [User.total_posts,{post_title: post_content}]
        User.all_posts.append(this_post)

    def delete_a_post(self):
        print(self.posts)
        if len(self.posts) < 1:
            return f"{self._name}, have no posts at this time"
        post_choice = int(input("which post would you like to delete?"))
        if 0 <= post_choice <= len(self.posts):
            self.posts.pop(post_choice - 1)
        print(self.posts)
    


