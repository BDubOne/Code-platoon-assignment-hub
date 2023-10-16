from classes.User import User
from classes.PremiumUser import PremiumUser
from classes.FreeUser import FreeUser

bryan = FreeUser("Bryan", 37, "Code Platoon/Father", "email@email.com", "37373737", "Pani Puri", "Paul Foster Case")

annie = FreeUser("Annie", 48, "VA Whole Health", "email@email.com", "37373737", "burritos", "nature")

unity = PremiumUser("Unity", 17, "school", "email@email.com", "37373737", "Mashed Potatoes", "Metallica", [], "5555-5555-5555-5555")

max = PremiumUser("Max", 15, "school", "email@email.com", "37373737", "milkshakes", "Anime", [], "5555-5555-5555-5555")

eko = FreeUser("Eko", 15, "school", "email@email.com", "37373737", "milkshakes", "Kobe Bryant")

print(max._ccard)
bryan.create_a_post()
bryan.create_a_post()
bryan.create_a_post()
max.delete_a_post()
eko.create_a_post()
unity.create_a_post()
bryan.create_a_post()
print(User.all_posts)