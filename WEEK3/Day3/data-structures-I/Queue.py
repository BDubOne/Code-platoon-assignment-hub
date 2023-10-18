####API####
# enqueue - add item to beginning
# dequeue - remove and return item from end
# peek - return last item
# size - return number of items
# is_empty - True if no items, False otherwise

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self,item):
        self.q.insert(0, item)

    def dequeue(self):
        removed = self.q.pop()
        return f'you have removed: {removed}'

    def peek(self):
        return f'{self.q[-1]} is at the head of the queue'

    def size(self):
        pass

    def is_empty(self):
        pass