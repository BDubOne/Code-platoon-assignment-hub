from classes.User import User

class PremiumUser(User):
    total_premium = 0
    def __init__(self, name, age, occupation, email, phone, hobby, inspiration, posts, ccard):
        super().__init__(name, age, occupation, email, phone, hobby,inspiration, posts)
        PremiumUser.total_premium += 1
        self._ccard = ccard

    @property
    def get_ccard(self):
        return self._ccard
    @get_ccard.setter
    def set_ccard(self, new_ccard):
        if isinstance(new_ccard, int):
            self._ccard = new_ccard

    


        

