class Node:

    """Individual Node in our Linked List
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Linked List handler/Main class"""
    def __init__(self):
        self.head = None

    def __str__(self):
        return f"{self.value}"

    def insert(self, value):
        """insert into list. 
        If Node.next == None, we are at the end of the list """
        new_node = Node(value)
        old_node = self.head
        self.head = new_node
        self.head.next = old_node

    def print_all_items_in_list(self):
        """insert value as new node into list"""
        current = self.head
        while(current is not None):
            print(current)
            current = current.next #At the end of the list, current.next is None, so current is set to NNone
        

    def search(self, value):
        """find a node in the list with 'value'"""

test_node = Node("hello world")
print(test_node.value)
print(test_node.next)
my_list = LinkedList()

user = {"name": "Alice", "email": "alice@gmail.com"}
my_list.insert(user)
my_list.insert("hello world")
my_list.insert("goodbye")
print(my_list.head.value)
print(my_list.head.next.value)
print(my_list.head.next.next.value)
