import pytest
from Stack import Stack
from Queue import Queue
from LinkedList import LinkedList, Node

#"""Testing the Node Class"""

def test_node_creation():
    node = Node(42)
    assert node.value == 42
    assert node.next is None
   

#"""Testing LinkedList Class"""

def test_linkedlist_init():
    linked_list = LinkedList()
    assert linked_list.head is None

def test_linked_insert():
    linked_list = LinkedList()

    #beginning insert
    linked_list.insert("hello world")
    assert str(linked_list) == "hello world"
    #end insert
    linked_list.insert(42)
    assert str(linked_list) == "hello world --> 42"
    #Insert Middle
    linked_list.insert("goodbye")
    assert str(linked_list) == "hello world --> 42 --> goodbye"

def test_list_remove():
    linked_list = LinkedList()
    linked_list.insert(42)
    linked_list.insert("the answer")
    linked_list.insert("test list")


    linked_list.remove("test list")
    assert str(linked_list) == "42 --> the answer"

    linked_list.remove(42)
    assert str(linked_list) == "the answer"

    linked_list.remove("the answer")
    assert str(linked_list) == ""

    with pytest.raises(ValueError):
        linked_list.remove("the answer")
    
def test_list_search():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    
    found_node = linked_list.search(3)
    assert found_node is not None
    assert found_node.value == 3

    not_found_node = linked_list.search(42)
    assert not_found_node is None


#"""Testing the Queue Class"""
@pytest.fixture
def empty_queue():
    return Queue()

@pytest.fixture
def queue_with_items():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.enqueue("d")
    return queue

def test_enqueue(empty_queue):
    empty_queue.enqueue(["e","f","g"])
    assert empty_queue.peek() == ["e","f","g"]

def test_dequeue(queue_with_items, empty_queue):
    queue_with_items.dequeue()
    assert queue_with_items.peek() == "d"
    assert queue_with_items.q[-1] == "b"
    queue_with_items.dequeue()
    assert queue_with_items.q[-1] == "c"
    empty_queue.enqueue('a')
    assert empty_queue.dequeue() == 'a'

def test_peek01(queue_with_items, empty_queue):
    assert queue_with_items.peek() == "d"
    empty_queue.enqueue("h")
    assert empty_queue.peek() == "h"

def test_size01(queue_with_items, empty_queue):
    queue_with_items.enqueue("i")
    empty_queue.enqueue("j")
    assert queue_with_items.size() == 5
    assert empty_queue.size() == 1

def test_is_empty01(queue_with_items, empty_queue):
    assert queue_with_items.is_empty() == False
    assert empty_queue.is_empty() == True
    queue_with_items.dequeue()
    queue_with_items.dequeue()
    queue_with_items.dequeue()
    queue_with_items.dequeue()
    assert queue_with_items.is_empty() == True




# """Testing the Stack Class"""
@pytest.fixture
def empty_stack():
    return Stack()

@pytest.fixture
def stack_with_items():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack

def test_push(empty_stack):
    empty_stack.push(42)
    assert empty_stack.peek() == 42

def test_pop(stack_with_items):
    item = stack_with_items.pop()
    assert item == 3
    assert stack_with_items.size() == 2

def test_peek(stack_with_items):
    item = stack_with_items.peek()
    assert item == 3
    assert stack_with_items.size() == 3

def test_size(empty_stack, stack_with_items):
    assert empty_stack.size() == 0
    assert stack_with_items.size() == 3

def test_is_empty(empty_stack, stack_with_items):
    assert empty_stack.is_empty() == True
    assert stack_with_items.is_empty() == False
