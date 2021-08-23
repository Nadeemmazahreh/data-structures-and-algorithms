from linkedlist import __version__
from linkedlist.linked_list import *
import pytest


def test_kth_greater_than_length():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)
    n1.next = n2
    n2.next = n3
    ll = LinkedList(n1)
    with pytest.raises(Exception) as excinfo:
        ll.kth_from_end(5)
    assert 'k is greater than the length of the linked list' == str(excinfo.value)


def test_kth_same_length():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)
    n1.next = n2
    n2.next = n3
    ll = LinkedList(n1)
    actual = ll.kth_from_end(2)
    expected = 1
    assert actual == expected

def test_k_not_positive():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)
    n4 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    ll = LinkedList(n1)
    with pytest.raises(Exception) as excinfo:
        ll.kth_from_end(-1)
    assert 'K is a negative value' == str(excinfo.value)


def test_ll_size_one():
    n1 = Node(1)
    ll = LinkedList(n1)
    actual = ll.kth_from_end(0)
    expected = 1
    assert actual == expected

def test_happy_path():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)
    n4 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    ll = LinkedList(n1)
    actual = ll.kth_from_end(2)
    expected = 2
    assert actual == expected





