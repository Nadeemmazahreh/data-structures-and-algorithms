
class Node:

    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head = None):
        self.head = head


    def append(self,value):
        currnet = self.head
        prev = None
        while currnet:
            prev = currnet
            currnet = currnet.next

        if prev:
            prev.next = Node(value)

        else:
            self.head = Node(value)


    def insert_before(self,value,newValue):
        newNode = Node(newValue)
        flag = True
        try:
            if self.head.value == value:
                newNode.next = self.head
                self.head = newNode
                current = None
                flag = False

            else:
                prev = self.head
                current = self.head.next

        except:
            current = None

        while current:
            if current.value == value:
                prev.next = newNode
                newNode.next = current
                break

            else:
                prev = current
                current = current.next

        if not current and flag:
            raise Exception('Value not found')


    def insert_after(self,value,newValue):

        newNode = Node(newValue)

        current = self.head

        while current:
            if current.value == value:
                newNode.next = current.next
                current.next = newNode
                break

            else:
                current = current.next

        if not current:
            raise Exception('Value not found')


    def kth_from_end(self,k):

        current = self.head
        prev = self.head
        n = 0

        if k < 0:
            raise Exception('K is a negative value')

        while current:
            current = current.next

            if n == k+1:
                prev = prev.next

            else:
                n += 1

        if n == k+1:
            return prev.value

        else:
            raise Exception('k is greater than the length of the linked list')


ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next= Node(3)
print(ll.kth_from_end(0))





