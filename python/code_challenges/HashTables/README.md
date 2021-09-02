# Hashtables
  In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

## Challenge
Implement a hash table map with the following methods:
  1- add
  2- get
  3- contains
  4- hash

## Approach & Efficiency

time: O(1)
space: O(n)

## API

add: This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
get: This method returns Value associated with that key in the table.
contains: This method returns Boolean, indicating if the key exists in the table already.
hash: This method returns Index in the collection for that key
