from linkedlist import __version__
from linkedlist.linked_list import *

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


def test_version():
    assert __version__ == '0.1.0'


