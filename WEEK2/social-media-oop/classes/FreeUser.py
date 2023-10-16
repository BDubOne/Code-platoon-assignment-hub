from classes.User import User

class FreeUser(User):
    free_list = []
    total_free = 0
    def __init__(self, name, age, occupation, email, phone, hobby, inspiration, posts=[]):
        super().__init__(name, age, occupation, email, phone, hobby,inspiration, posts)
        FreeUser.total_free += 1


    def create_a_post(self):
        if len(self.posts) >= 2:
            return f'sorry {self._name}. You need to become a Premium User in order to post more content'
        post_title = input("What is your post title?")
        post_content = input("What do you have to say?")
        User.total_posts += 1
        this_post = [User.total_posts,{post_title: post_content}]
        User.all_posts.append(this_post)
        self.posts.append(this_post)