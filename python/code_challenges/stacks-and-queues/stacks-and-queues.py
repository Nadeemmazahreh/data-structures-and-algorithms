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
           return 'The Queue is empty'

    def peek(self):
        try:
           return self.front.value

        except :
            return 'The Queue is empty'

    def isEmpty(self):
        return self.front == None




if __name__ == "__main__":

    stack = Stack()
    stack.push(3)
    stack.push(-7)
    stack.push('d')
    print(stack.pop())

    queue = Queue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    print(queue.peek()) 
    # print(queue.front.value)
