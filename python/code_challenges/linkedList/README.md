# Challenge Summary
    Append: write a function that adds a new node to the end of the linked list
    Insert after: write a function that inserts a node after a specific value in a linked list
    Insert Before: write a function that inserts a node before a specific value in a linked list
    Kth_from_end: write a function that takes an argument( a number k as a parameter) and Return the node’s     value that is k places from the tail of the linked list.
    Zip_list: Create a function that takes 2 linked lists as an argument and zips the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

## Whiteboard Process
![image](Code_challenge_6_append.PNG)
![image](Code_challenge_6_insert_after.PNG)
![image](Code_challenge_6_insert_before.PNG)
![image](Code_challenge_7.PNG)
![image](Code_challenge_8.PNG)

## Approach & Efficiency
    for all the challenges the bigO of time is O(n) and the big of space is O(1)

    Zip_list: time O(n)
              space O(n)

## Solution

    Append:
        ll = LinkedList()
        ll.head = Node(1)
        ll.head.next = Node(2)
        ll.head.next.next= Node(3)
        ll.append(10)
        print(ll.head.next.next.next.value)

    output: 10

    Insert After
        ll = LinkedList()
        ll.head = Node(1)
        ll.head.next = Node(2)
        ll.head.next.next= Node(3)
        ll.insert_after(1,10)
        print(ll.head.next.value)

    output: 10

    Insert before
        ll = LinkedList()
        ll.head = Node(1)
        ll.head.next = Node(2)
        ll.head.next.next= Node(3)
        ll.insert_before(2,10)
        print(ll.head.next.value)

    output: 10


    Kth_from_end

        ll = LinkedList()
        ll.head = Node(1)
        ll.head.next = Node(2)
        ll.head.next.next= Node(3)
        print(ll.kth_from_end(0))

    output: 3


    Zip_list:

        ll1 = LinkedList()
        ll1.append(1)
        ll1.append(3)
        ll2 = LinkedList()
        ll2.append(2)
        ll2.append(4)
        print(ll1.__str__())
        print(ll2.__str__())
        print(zipLists(ll1, ll2))

    output: (1)->(2)->(3)->(4)
