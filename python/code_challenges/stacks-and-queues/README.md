# Stacks and Queues
A stack and Queues are a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

## Challenge
1. Create a Stack class that has (push, pop, peek, isEmpty) methods.

2. Create a Queue class that has (enqueue, dequeue, peek, isEmpty) methods.

## Approach & Efficiency

all of the methods
time: O(1)
Space: O(1)

## API

### Stack:
1. **push** which takes any value as an argument and adds a new node with that value to the top of the stack.

2. **pop** that does not take any argument, removes the node from the top of the stack, and returns the node’s value.

3. **peek** that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.

4. **isEmpty** that takes no argument, and returns a boolean indicating whether or not the stack is empty.

### Queue:
1. **enqueue** which takes any value as an argument and adds a new node with that value to the back of the queue.

2. **dequeue** that does not take any argument, removes the node from the front of the queue, and returns the node’s value.

3. **peek** that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.

4. **isEmpty** that takes no argument, and returns a boolean indicating whether or not the queue is empty.
