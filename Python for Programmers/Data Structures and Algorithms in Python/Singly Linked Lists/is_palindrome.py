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

    def is_palindrome_ptr(self):
        # check if LL is not empty
        if self.head:
            # assign variables to head of LL
            p = self.head
            q = self.head
            # create an empty list
            prev = []

            i = 0
            # move to end of LL while storing values in list
            while q:
                prev.append(q)
                q = q.next
                i += 1
            # save the value of the last item
            q = prev[i-1]

            count = 1

            # run while loop to half of list
            while count <= i//2 + 1:
                # go from back of list (-1) and front of LL
                # items should be the same
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True


llist = LinkedList()
llist.append("R")
llist.append("A")
llist.append("C")
llist.append("E")
llist.append("C")
llist.append("A")
llist.append("R")

print(llist.is_palindrome_string())
print(llist.is_palindrome_stack())
print(llist.is_palindrome_ptr())

print("\n\n")

llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("C")

print(llist_2.is_palindrome_string())
print(llist_2.is_palindrome_stack())
print(llist_2.is_palindrome_ptr())
