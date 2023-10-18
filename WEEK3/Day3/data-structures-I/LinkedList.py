from Node import Node

####API####
# insert - add node to beginning (or end)
# search - find and return a given node
# remove - remove a given node
# size - return number of nodes
# is_empty - True if no nodes, False otherwise

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,position,data):
        new_node = Node(data)
        if position == 0 or not self.head:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0

        while current.next and count < position - 1:
            current = current.next
            count += 1

        new_node.next = current.next
        current.next = new_node
        
            
           