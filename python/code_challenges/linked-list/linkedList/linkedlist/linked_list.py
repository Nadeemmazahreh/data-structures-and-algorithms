
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




def zip_List(LinkedList1, LinkedList2):
    newList = LinkedList()
    current = LinkedList1.head

    while current:
        newList.append(current.value)
        newList.append(0)
        current = current.next

    current = newList.head
    counter = 0
    current2 = LinkedList2.head

    while current:
        if  counter % 2 == 1:
            current.value = current2.value
            current = current.next
            current2 = current.next
            counter += 1

    return newList


ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next= Node(3)

ll2 = LinkedList()
ll2.head = Node(4)
ll2.head.next = Node(5)
ll2.head.next = Node(6)

ll_zip = zip_List(ll1,ll2)
print(ll_zip.head.value)

print('hello')





