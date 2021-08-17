class Node:

    def __init__(self ,value):
        self.value = value
        self.left = None
        self.right = None

def FizzBuzzTree(kAryTree):
    queue = []
    result =[]
    if root is None:
        print('tree is empty')

    queue.append(root)
    while(len(queue) > 0):

        node = queue.pop(0)

        if node.value % 3 == 0:
            node.value = 'Fizz'
        elif node.value % 5 == 0:
            node.value = 'Buzz'
        elif node.value % 3 == 0 and node.value % 5 == 0:
            node.value = 'FizzBuzz'
        else:
            node.value = str(node.value)

        result.append(node.value)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result


root = Node(9)
root.left = Node(15)
root.right = Node(10)
root.left.left = Node(11)
root.left.right = Node(20)
root.right.right = Node(3)


print ("Level Order Traversal of binary tree is -")
print(FizzBuzzTree(root))


