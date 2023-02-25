from stackpractice import Stack


def convert_number(number):
    is_converted = False
    number_stack = Stack()
    number_string = ""

    while not is_converted:
        integer = number // 2
        remainder = number % 2

        number_stack.push(str(remainder))

        if integer != 0:
            number = integer
        else:
            is_converted = True

    while not number_stack.is_empty():
        number_string += number_stack.pop()

    return number_string


print(convert_number(99))
print(convert_number(56))
print(convert_number(2))
print(convert_number(32))
print(convert_number(10))


