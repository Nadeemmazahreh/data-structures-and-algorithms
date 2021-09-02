
import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return f'{values}'

class Hashtable:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size

    def hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp_value = sum_of_asccii * 19
        hashed_key = temp_value % self.size
        return hashed_key

    def add(self, key, value):
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].add((key,value))

    def contains(self,key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            self.map[hashed_key].head.data[0]
            current=self.map[hashed_key].head
            while current:
                if current.data[0]==key:
                    return True
                else:
                    current=current.next
        return False

    def get(self,key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            self.map[hashed_key].head.data[0]
            current=self.map[hashed_key].head
            while current:
                if current.data[0]==key:
                    return current.data[1]
                else:
                    current=current.next
        return None


def test_add_hashtable():
    HT = Hashtable(10)
    HT.add('Tarek', 30)
    assert HT.get('Tarek')==30

def test_get_hashtable():
    HT = Hashtable(10)
    HT.add('Saif', 20)
    actual=HT.get('Saif')
    expected=20
    assert actual==expected

def test_get_hashtable_incorrect_key():
    HT = Hashtable(10)
    actual= HT.get('Fadi')
    expected=None
    assert actual==expected


def test_collision_hashtable():
    HT = Hashtable(10)
    HT.add('Fares',10)
    actual=HT.contains('Fares')
    expected=True
    assert actual==expected

def test_collision_value_hashtable():
    HT = Hashtable()
    actual=HT.get('hamad')
    expected=29
    assert actual==expected


def test_collision_value_hashtable():
    HT = Hashtable(10)
    actual= HT.hash('Fares')
    expected=3
    assert actual==expected
