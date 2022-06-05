"""
Convert a decimal number to binary using a stack.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


def convert_int_to_bin(dec_num):
    # if decimal number is 0 simply return 0
    if dec_num == 0:
        return 0

    # otherwise we create a stack object and initialize a string to store final result to empty
    stack = Stack()
    binary_num = ""
    # we grab the first remainder
    stack.push(dec_num % 2)
    # if further division is needed to get the floor to 0 we keep using floor as dividend
    while dec_num // 2 is not 0:
        dec_num = dec_num // 2
        # add the remainder of this number to the stack
        stack.push(dec_num % 2)

    # now start popping off the stack and inserting into the string
    while not stack.is_empty():
        binary_num += str(stack.pop())

    # return the resulting string
    return binary_num


print(convert_int_to_bin(121))
print(convert_int_to_bin(56))
print(convert_int_to_bin(2))
print(convert_int_to_bin(32))
print(convert_int_to_bin(10))
print(int(convert_int_to_bin(56),2)==56)
