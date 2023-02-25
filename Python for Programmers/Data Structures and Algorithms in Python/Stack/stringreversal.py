from stackpractice import Stack


# reversing a string
def string_reversal(string):
    # make a stack object
    string_stack = Stack()
    reversed_string = ""

    # iterate through the string and push each character onto stack
    for char in string:
        string_stack.push(char)

    # while the stack has characters pop them off add to empty string
    while not string_stack.is_empty():
        reversed_string += string_stack.pop()

    # get the now reversed string
    return reversed_string


print(string_reversal("python"))
