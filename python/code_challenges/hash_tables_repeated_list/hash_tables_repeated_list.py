import re

class Node:
    def __init__(self, value):
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

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
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
        self.map[hashed_key].append((key,value))

    def contains(self,key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            self.map[hashed_key].head.value[0]
            current=self.map[hashed_key].head
            while current:
                if current.value[0]==key:
                    return True
                else:
                    current=current.next
        return False

    def get(self,key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            self.map[hashed_key].head.value[0]
            current=self.map[hashed_key].head
            while current:
                if current.value[0]==key:
                    return current.value[1]
                else:
                    current=current.next
        return None

def repeated_word(string=None):
    if string == None :
        return 'the string is empty'
    hashtable = Hashtable(1024)

    string = re.sub('\W+', ' ', string).lower().split()

    for word in string:

        if hashtable.contains(word):
            return word
        else:

            hashtable.add(word, True)

string="Once upon a time, there was a brave princess who..."

print(repeated_word(string))

