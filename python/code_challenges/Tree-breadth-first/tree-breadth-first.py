class Node:

    def __init__(self ,value):
        self.value = value
        self.left = None
        self.right = None

def TreeBreadthFirst(root):

    queue = []
    result =[]

    if root is None:
        print('tree is empty')

    queue.append(root)

    while(len(queue) > 0):

        result.append(queue[0].value)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    print(result)

root = Node(8)
root.left = Node(2)
root.right = Node(9)
root.left.left = Node(11)
root.left.right = Node(20)
root.right.right = Node(3)


print ("Level Order Traversal of binary tree is -")
TreeBreadthFirst(root)
