from Stack import Stack
from Queue import Queue

my_stack = Stack()
print('hello')
my_stack.push('hello')
Stack.print_base(my_stack)
# Stack.pop(my_stack)
my_stack.print_base()
my_stack.peek()
my_q = Queue()
my_q.enqueue("My first Pizza Order")
my_q.enqueue("My second Pizza Order")
my_q.enqueue("My third pizza order")
print(my_q.q)
print(my_q.dequeue())
print(my_q.peek())
print(my_q.q)

