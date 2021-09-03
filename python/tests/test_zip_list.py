
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
def zip_list(ll1, ll2):

    curr1 = ll1.head
    curr2 = ll2.head

    if curr1 == None or curr2 == None:
        if curr1:
            return ll1.__str__()
        elif curr2:
            return ll2.__str__()
        else:
         return "Both of the linked list is empty"

    list = []
    while curr1 or curr2:
        if(curr1):
            list+=[curr1.value]
            curr1 = curr1.next
        if(curr2):
            list+=[curr2.value]
            curr2 = curr2.next
    z=''
    for i in list:
      z+=f'({i})->'
    z+='None'
    return z


def test_happy_path():
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    actual=zip_list(ll1, ll2)
    expected='(1)->(2)->(3)->(4)->(5)->(6)->None'

    assert actual==expected




def test_edge_case():
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    actual=zip_list(ll1, ll2)
    expected='(1)->(2)->(3)->(4)->(5)->None'

    assert actual==expected
