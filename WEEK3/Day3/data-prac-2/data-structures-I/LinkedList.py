class Node:
    """Each Node Contains a pointer to the one before it and the one after it for a bidirectional method of insertion and removal in the Linked List class"""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
      

class LinkedList:
    """Initialize an instance of a Node in the Linked List"""
    def __init__(self):
        self.head = None

    def __str__(self):
        """This string method relies on a while loop so that it can trace the nodes and return each one connected in the Linked List"""
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        result = " --> ".join(elements)
        return result
        
    def insert(self, value, position=0):

        #Currently, this only inserts an item at the end. I haven't figured out how to make it work when I try to make it bidirectional
        """This Method assumes a position of 0 and that the element will be inserted at the end of the linked list. It also can take in a positional argument for adding a new node to the beginning of the linked list """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove(self, value):

        '''method for removing from either head or previous.
        Begin with Head'''
        if self.head is None:
            raise ValueError(f'{value} not found in linked list')
        
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError(f"{value} not found in linked list")
    
    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current.value
            current = current.next 
        return f"{value} is not found in the list"
    

            
        



####API####
# insert - add node to beginning (or end)
# search - find and return a given node
# remove - remove a given node
# size - return number of nodes
# is_empty - True if no nodes, False otherwise