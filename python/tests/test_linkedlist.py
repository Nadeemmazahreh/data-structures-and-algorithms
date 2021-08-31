# from code_challenges.linkedList.linked_list import *


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


def test_add_to_end():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)
    n1.next = n2
    n2.next = n3
    ll = LinkedList(n1)
    ll.append(5)
    actual = n3.next.value
    expected = 5
    assert actual == expected

def test_add_multiple_to_end():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)
    n1.next = n2
    n2.next = n3
    ll = LinkedList(n1)
    ll.append(5)
    ll.append(7)
    actual1 = n3.next.value
    expected1 = 5
    assert actual1 == expected1

    actual2 = n3.next.next.value
    expected2 = 7
    assert actual2 == expected2

def test_insert_before():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)
    n1.next = n2
    n2.next = n3
    ll = LinkedList(n1)
    ll.insert_before(2,3)

    actual = n1.next.value
    expected = 3
    assert actual == expected

def test_insert_before_first_node():
    n1 = Node(1)
    ll = LinkedList(n1)
    ll.insert_before(1,3)

    actual = ll.head.value
    expected = 3
    assert actual == expected

def test_insert_after():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)
    n1.next = n2
    n2.next = n3
    ll = LinkedList(n1)
    ll.insert_after(2,3)

    actual = n2.next.value
    expected = 3
    assert actual == expected

def test_insert_after_last_node():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)
    n1.next = n2
    n2.next = n3
    ll = LinkedList(n1)
    ll.insert_after(4,3)

    actual = n3.next.value
    expected = 3
    assert actual == expected



