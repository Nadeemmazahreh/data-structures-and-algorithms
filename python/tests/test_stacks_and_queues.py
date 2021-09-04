
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None

    def push(self,value):
        node=Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        try:
           popValue=self.top.value
           self.top=self.top.next
           return popValue
        except:
            return 'empty stack'

    def peek(self):
        try:
            return self.top.value
        except:
            return 'empty stack'

    def isEmpty(self):
        return self.top==None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self, value):
        node = Node(value)
        if not self.front:

            self.front = node
            self.rear = node
        else:

            self.rear.next = node
            self.rear = node

    def dequeue(self):
        try:
           dequeueValue=self.front.value
           self.front=self.front.next
           return dequeueValue
        except :
           return 'empty queue'

    def peek(self):
        try:
           return self.front.value

        except :
            return 'empty queue'

    def isEmpty(self):
        return self.front == None


# stack = Stack()
# stack.push(5)
# stack.push(-10)
# stack.push('m')

# queue = Queue()
# queue.enqueue(8)
# queue.enqueue('r')
# queue.enqueue(-4)
# queue.enqueue(6)

def test_push():
    stack = Stack()
    stack.push('m')
    actual = stack.top.value
    expected = 'm'
    assert actual == expected

def test_pop():
    stack = Stack()
    stack.push('m')
    stack.push(5)
    actual = stack.pop()
    expected = 5
    assert actual == expected
    assert stack.top.value == 'm'

# def test_is_empty_true():
#     stack = Stack()
#     stack.push(5)
#     stack.push(-10)
#     stack.push('m')
#     stack.pop()
#     stack.pop()
#     stack.pop()
#     assert stack.isEmpty() == True


def test_peek_stack():
    stack = Stack()
    stack.push(5)
    stack.push(-10)
    stack.push('m')
    actual = stack.peek()
    expected = 'm'
    assert actual == expected
    assert stack.top.value == 'm'

def test_is_empty_stack():
    stack = Stack()
    stack.push(5)
    stack.push(-10)
    stack.push('m')
    assert stack.isEmpty() == False

def test_stack_exception():
    stack = Stack()
    stack.push(5)
    stack.push(-10)
    stack.push('m')
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.pop()=='empty stack'
    assert stack.peek()=='empty stack'


def test_enqueue():
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue('r')
    queue.enqueue(-4)
    queue.enqueue(6)
    assert queue.rear.value == 6
    assert queue.front.value == 8


def test_dequeue():
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue('r')
    queue.enqueue(-4)
    queue.enqueue(6)
    data = queue.dequeue()
    assert data == 8
    assert queue.front.value == 'r'

def test_peek_queue():
    queue = Queue()
    queue.enqueue(8)
    assert queue.peek()==8


