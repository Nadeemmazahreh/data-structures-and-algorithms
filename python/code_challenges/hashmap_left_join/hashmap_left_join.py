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

def left_join(hashtable1,hashtable2):
    arr=[]
    if hashtable1.map == hashtable1.size*[None] or hashtable2.map == hashtable2.size*[None] :
        return 'one of the hash table is empty'
    for item in hashtable1.map:
        if item:
            arr2=[]
            arr2.append(item.head.value[0])
            arr2.append(hashtable1.get(item.head.value[0]))
            arr2.append(hashtable2.get(item.head.value[0]))
            arr.append(arr2)
    return arr

if __name__ == "__main__":
    ht1 = Hashtable(10)
    ht1.add('fond', 'enamored')
    ht1.add('wrath', 'anger')
    ht1.add('diligent', 'employed')
    ht1.add('outfit', 'grap')
    ht1.add('guide', 'usher')
    ht2 = Hashtable(10)
    ht2.add('fond', 'averse')
    ht2.add('wrath', 'delight')
    ht2.add('diligent', 'idle')
    ht2.add('guide', 'follow')
    ht2.add('flow', 'jam')

    print(left_join(ht1,ht2))
