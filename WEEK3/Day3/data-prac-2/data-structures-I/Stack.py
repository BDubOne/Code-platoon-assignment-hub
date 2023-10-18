class Stack:
    def __init__(self):
        """Stack consists of a base list"""
        self.base = []
    
    def __str__(self):
        """represents the instance of Stack by returning base list"""
        return f'{self.base}'
    

    def push(self, item):
        """appends an item to the end of the base list"""
        return self.base.append(item)

        
    def pop(self):
        """removes the last item of the list (LIFO)"""
        return self.base.pop()

    def peek(self):
        """returns the last item of the list"""
        return self.base[-1]
    def size(self):
        """returns the length of the list"""
        return len(self.base)
    
    def is_empty(self):
        """returns boolean value for whether the list is empty"""
        return len(self.base) == 0
    ####API####
# push - add item to top
# pop - remove and return item from top
# peek - return top item
# size - return number of items
# is_empty - True if no items, False otherwise


