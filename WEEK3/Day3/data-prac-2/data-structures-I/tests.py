import pytest
from Stack import Stack
from Queue import Queue

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

def test_dequeue(queue_with_items):
    queue_with_items.dequeue()
    assert queue_with_items.peek() == "d"
    assert queue_with_items.q[-1] == "b"
    queue_with_items.dequeue()
    assert queue_with_items.q[-1] == "c"

def test_peek(queue_with_items, empty_queue):
    assert queue_with_items.peek() == "d"
    empty_queue.enqueue("h")
    assert empty_queue.peek() == "h"

def test_size(queue_with_items, empty_queue):
    assert queue_with_items.size() == 5
    assert empty_queue.size() == 2

def test_is_empty(queue_with_items, empty_queue):
    assert queue_with_items.is_empty == False
    empty_queue.dequeue()
    empty_queue.dequeue()
    assert empty_queue.is_empty() == True




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
