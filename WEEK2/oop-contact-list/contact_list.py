class ContactList:
    
    shared_contacts = {}
    my_friend_list = []
    work_buddies = []
    total_contacts = 0
    
    def __init__(self, name="John Doe", number="777-7777"):
        ContactList.total_contacts += 1
        self._id = ContactList.total_contacts
        self._name = name
        self._number = number
        ContactList.shared_contacts[self._id] = self
    
    def __str__(self):
        return f" {self._id}: 'name' : {self._name}, 'number': {self._number}"
    
    @property
    def get_name(self):
        return self._name
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name

    @property
    def get_number(self):
        return self._number
    @get_number.setter
    def set_number(self, new_number):
        self._number = new_number

    @staticmethod
    def view_all_contacts():
        for index in ContactList.shared_contacts:
            print(ContactList.shared_contacts[index])

    
    def add_contact():
        
        
        print("I'm gonna need your name and number")
            
        name = input("what is your name?")
        number = str(input("what is your phone number?"))

        friend_prompt = '''
        
        ---where do I know you from?---
        1. work     |     2. life
        '''
        print(friend_prompt)
        choice = int(input("choose a number"))
        if choice == 1:
            path = ContactList.my_friend_list
        elif choice == 2:
            path = ContactList.work_buddies

        ContactList.view_all_contacts()
        print(path)


        new_contact = ContactList(name, number)
        path.append(new_contact)

    def remove_contact():
        ContactList.view_all_contacts()
       
        index = int(input('Which contact would you like to remove?     '))
        ContactList.shared_contacts.pop(index)
        ContactList.view_all_contacts()

bryan = ContactList("Bryan", "555-5555")
annie = ContactList("Annie", "999-9999")
ContactList.view_all_contacts()
ContactList.remove_contact()

      

       



    
