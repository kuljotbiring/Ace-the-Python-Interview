class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def is_palindrome_string(self):
        s = ""
        p = self.head

        while p:
            s += p.data
            p = p.next
        return s == s[::-1]

    def is_palindrome_stack(self):
        p = self.head
        s = []

        while p:
            s.append(p.data)
            p = p.next

        p = self.head
        while p:
            val = s.pop()
            if p.data != val:
                return False
            p = p.next

        return True
