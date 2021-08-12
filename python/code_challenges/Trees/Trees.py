class Node:
   def __init__(self, value=None):
      self.left = None
      self.right = None
      self.value = value

class BinaryTree:

    def preOrder(self, root):

        print(root.value)

        if root.left:
            self.preOrder(root.left)

        if root.right:
            self.preOrder(root.right)


    def inOrder(self, root):

        if root.left:
            self.inOrder(root.left)

        print(root.value)

        if root.right:
            self.inOrder(root.right)


    def postOrder(self, root):

        if root.left:
            self.postOrder(root.left)

        if root.right:
            self.postOrder(root.right)

        print(root.value)

class BinarySearchTree(BinaryTree):

    def add(self, value):
        if self.root ==None:
            self.root=Node(value)
        else:
            node = Node(value)

            def traverse(root):
                if node.value < root.value:

                    if root.left:
                        root=root.left
                        traverse(root)
                    else:
                        root.left=node
                else:

                    if root.right:
                        root=root.right
                        traverse(root)
                    else:
                        root.right=node

            traverse(self.root)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
BT = BinaryTree()
BT.preOrder(root)

print("\nInorder traversal of binary tree is")
BT.inOrder(root)

print("\nPostorder traversal of binary tree is")
BT.postOrder(root)

BST = BinarySearchTree()
BST.add(50)
BST.add(30)
BST.add(20)
BST.add(40)
BST.add(70)
BST.add(60)
BST.add(80)

print("\nInorder traversal of binary Search tree is")
BST.preOrder()



