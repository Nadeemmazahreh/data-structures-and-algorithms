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
            return 'The Stack is empty'

    def peek(self):
        try:
            return self.top.value
        except:
            return 'The Stack is empty'

    def isEmpty(self):
        return self.top==None

class PseudoQueue:
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()

    def enqueue(self,value=None):
        if value == None:
            return 'Please put a value'

        self.front.push(value)

    def dequeue(self):

        if not self.front.top:
            return 'The Queue is empty'

        while self.front.top:


            self.rear.push(self.front.pop())

        dequeuevalue = self.rear.pop()

        while self.rear.top:


            self.front.push(self.rear.pop())

        return dequeuevalue


    def __str__(self):
        current=self.front.top
        x=''
        while current:
            if not current.next:
                x=x+f'( {current.value} )'
                current=current.next
            else:
                x=x+f'( {current.value} ) -> '
                current=current.next
        return x


def test_enqueue_happypath():
    queue = PseudoQueue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    actual = queue.__str__()
    expected = '( 6 ) -> ( -4 ) -> ( hi ) -> ( 8 )'
    assert actual == expected

def test_enqueue_Expected_failure():
    queue = PseudoQueue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    actual = queue.__str__()
    expected = '( 6 ) -> ( -4 ) -> ( hi )'
    assert actual != expected

def test_enqueue_edge_case():
    queue2 = PseudoQueue()
    actual = queue2.enqueue()
    expected = 'Please put a value'
    assert actual == expected

def test_dequeue_happypath():
    queue = PseudoQueue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    dequeuevalue=queue.dequeue()
    actual = queue.__str__()
    expected = '( 6 ) -> ( -4 ) -> ( hi )'
    assert actual == expected
    assert dequeuevalue==8

def test_dequeue_Expected_failure():
    queue = PseudoQueue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    dequeuevalue=queue.dequeue()
    actual = queue.__str__()
    expected = '( 6 ) -> ( -4 ) -> ( hi ) -> ( 8 )'
    assert actual != expected
    assert dequeuevalue != 'hi'

def test_dequeue_edge_case():
    queue2 = PseudoQueue()
    actual = queue2.dequeue()
    expected = 'The Queue is empty'
    assert actual == expected
