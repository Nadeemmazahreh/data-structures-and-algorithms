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
