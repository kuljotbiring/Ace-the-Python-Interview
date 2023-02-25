class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


# my_stack = Stack()
# my_stack.push("A")
# my_stack.push("B")
# my_stack.push("C")
#
# print(my_stack.get_stack())
#
# print(my_stack.peek())
#
# my_stack.pop()

# print(my_stack.peek())
#
# print(my_stack.get_stack())
