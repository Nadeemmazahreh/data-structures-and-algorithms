from re import escape


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.treelist=[]

    def pre_order(self):

        output = ''
        if not self.root:
            return 'The Tree is empty'

        self.treelist=[]
        def traverse(node):
            nonlocal output
            output += str(node.value)
            self.treelist+=[(node.value)]

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)

        traverse(self.root)

        return output

    def post_order(self):
        output = ''
        if not self.root:
            return 'The Tree is empty'

        def traverse(node):
            nonlocal output

            if node.left:

                traverse(node.left)

            if node.right:
                traverse(node.right)

            output += str(node.value)


        traverse(self.root)

        return output

    def in_order(self):
        output = ''
        if not self.root:
            return 'The Tree is empty'

        def traverse(node):
            nonlocal output

            if node.left:

                traverse(node.left)

            output += str(node.value)

            if node.right:
                traverse(node.right)

        traverse(self.root)

        return output

    def max(self):
        self.max=0
        def traverse(node):

            if node.left:
              traverse(node.left)
              if node.left.value>self.max:
                self.max=node.left.value

            if node.right:
              traverse(node.right)
              if node.right.value>self.max:
                self.max=node.right.value

        traverse(self.root)

        if self.root.value>self.max:
          return self.root.value

        return self.max
