"""
Stack Data Structure.
"""


class Stack:
    # create a stack class
    def __init__(self):
        # initialize with empty list
        self.items = []

    # push operations append to end of the list
    def push(self, item):
        self.items.append(item)

    # pop removes the last item and returns it
    def pop(self):
        return self.items.pop()

    # returns True or False if the list is equal to an empty list
    def is_empty(self):
        return self.items == []

    # check is the list is not empty and then returns the item at the end
    # to view what it is.
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    # get the stack and returns the list elements
    def get_stack(self):
        return self.items


myStack = Stack()
myStack.push("A")
myStack.push("B")
print(myStack.get_stack())
myStack.push("C")
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())
