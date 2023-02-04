from stackpractice import Stack


# takes two parameters. the top of the stack and the current index of the string
# check to see if they match and returns true if they are. otherwise false
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False


# checks to see if string parenthesis are balanced
def is_paren_balanced(paren_string):
    # set initial values and create stack object
    is_balanced = True
    index = 0
    my_stack = Stack()

    # run loop while still string chars left and boolean is true
    while index < len(paren_string) and is_balanced:
        # save character in a variable
        paren = paren_string[index]

        # if the current character is an opening bracket push on stack
        if paren in "([{":
            my_stack.push(paren)

        # otherwise
        else:
            # if the stack is empty then parenthesis are not balanced
            if my_stack.is_empty():
                is_balanced = False
                break
            else:
                # check the top of the stack
                top = my_stack.pop()
                # if the two are not matching parenthesis
                if not is_match(top, paren):
                    # then it's not balanced
                    is_balanced = False
                    break

        # move forward in the string index
        index += 1

    # if the stack is now empty and is balanced is True - then matching parenthesis
    if my_stack.is_empty() and is_balanced:
        return True
    # other-wise parenthesis did not match
    else:
        return False
