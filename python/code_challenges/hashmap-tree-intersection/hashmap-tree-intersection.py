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


class Nodet:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class BinaryTree:
    def __init__(self):
        self.root = None


def find_intersection(tree1,tree2):
    arr=[]
    hashtable=Hashtable(1024)

    if tree1.root==None or tree2.root==None:
        return 'one of the tree is empty'

    def travers(node):
        if hashtable.contains(str(node.value)):
            nonlocal arr
            arr+=[node.value]
        else:
            hashtable.add(str(node.value),True)

        if node.left:
            travers(node.left)
        if node.right:
            travers(node.right)
    travers(tree1.root)
    travers(tree2.root)

    return arr


if __name__ == "__main__":
    tree1=BinaryTree()
    tree1.root=Nodet(3)
    tree1.root.left=Nodet(2)
    tree1.root.right=Nodet(8)
    tree1.root.right.right=Nodet(1)

    tree2=BinaryTree()
    tree2.root=Nodet(9)
    tree2.root.left=Nodet(10)
    tree2.root.right=Nodet(8)
    tree2.root.left.left=Nodet(3)
    tree2.root.right.right=Nodet(5)

    print(find_intersection(tree1,tree2))
