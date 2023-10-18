####API####
# push - add item to top
# pop - remove and return item from top
# peek - return top item
# size - return number of items
# is_empty - True if no items, False otherwise

class Stack:
    """stack!"""

    def __init__(self) -> None:
        self.base = []

    def push(self,item):
        self.base.append(item)

    def pop(self):
        if self.base:
            self.base.pop()
        return None

    def peek(self):
        '''peek'''
        if self.base:
            
            return self.base[-1]
        return None
    
    def print_base(stack):
        print("stack base: ", stack.base)
my_stack = Stack()
print('hello')
my_stack.push('hello')
Stack.print_base(my_stack)
# Stack.pop(my_stack)
Stack.print_base(my_stack)
print(Stack.peek(my_stack))
