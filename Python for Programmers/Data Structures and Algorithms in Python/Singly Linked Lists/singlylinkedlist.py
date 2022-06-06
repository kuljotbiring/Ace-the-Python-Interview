"""
All linked lists have nodes. Each node has two components - DATA & NEXT
DATA = allows a node to store an element of data
NEXT = a pointer from one node to another

- start of linked list referred to as HEAD
HEAD = pointer that points to beginning of the linked list

- last component of a linked list is a notation of null
NULL = terminates the linked list - we call it NONE - end of a linked list

INSERTION/DELETION beginning of linked list = O(1)
ACCESS ELEMENT = O(n)
CONTIGUOUS MEMORY = NO
"""


class Node:
    def __init__(self, data):
        self.data = data
        # set to none  - we change this as we use the node
        self.next = None


class LinkedList:
    def __init__(self):
        # points to first Node in the linked list
        self.head = None


