# Challenge Summary
Create a function that takes 2 binary trees as an input and returns all the values that are present in both trees in an array

## Whiteboard Process
![1](Code_challenge_32.jpg)

### Big O :

* Time--> O(n)
* space--> O(n)

## Solution

-verification
input = tree1,tree2
Expected output =[3,8]

```

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
```
    output: [3,8]
