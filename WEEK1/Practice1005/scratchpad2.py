

#tuple concat

old_tuple =(1, 2, 3)
new_item = 4
new_tuple = old_tuple+(new_item,)
print(new_tuple)

# what is difference between tuple and list in memory

# dictionaries


# print(jeff['age'])

people = [
    {
        'name': 'alice',
        'age': 44,
        'job': 'influencer',
    },
    {
        'name': 'bob',
        'age': 31,
        'job': 'dog walker',
    },
    {
        'name': 'carol',
        'age': 65,
        'job': 'life coach',
    },
]

# print(people)
# print(people[1]['name'])

def gimme_five():
    x = 4
    return 5
print(gimme_five() + 10)

kyle = {
    'name': 'kyle',
    'age': 45,
    'job': 'influencer',
    'action': gimme_five,
    'favorite_foods': [
        'sushi',
        'hamburgers'
    ],
    'dietary_restrictions': [{'allergies':
                                               ['peanuts', 'shellfish']}, {'doesnt_eat':
                                               ['vegetables', 'ketchup']}
                                               ]
}

#applying function to a dictionary item. Unnecessary when we get
#into classes

'''
print(kyle['action']())

class Person:
    def --init--(name):
        self.name = name
    def gimme_five(self)
        print(name)

kyle = new Person('kyle')
'''
def add_one(n):
    return n + 1

def describe_berries(n, color):
    print(f"I have {n} {color}berries.")

def print_them_all(*args):
    print(args)

       # print_them_all('alice', 'bob', 'carold')

def describe_berries(n=1, color="blue"):
            print(f'I have {n} {color}berries')

describe_berries(color="rasb", n=3)

def who_am_(**kwargs):
      for k in kwargs:
            print(f'My {k} is {kwargs[k]}')
who_am_(name='dan', age='20')

