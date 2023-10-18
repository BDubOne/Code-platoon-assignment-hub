
class Queue:
    def __init__(self):
        """create an instance of Queue with data stored in a list called q"""
        self.q = []

    def __str__(self):
        """prints the list called q"""
        return f"{self.q}"
    
    def enqueue(self, item):
        """adds an item to the beginning of q"""
        return self.q.insert(0, item)
    
    def dequeue(self):
        """remove an item from the end of q"""
        return self.q.pop()
    
    def peek(self):
        """returns the last item added to the list"""
        return self.q[0]
    
    def size(self):
        """returns the length of q (size of the queue instance)"""
        return len(self.q)
    
    def is_empty(self):
        """returns a boolean of whether the queue is empty or not"""
        return len(self.q) == 0
####API####
# enqueue - add item to beginning
# dequeue - remove and return item from end
# peek - return last item
# size - return number of items
# is_empty - True if no items, False otherwise