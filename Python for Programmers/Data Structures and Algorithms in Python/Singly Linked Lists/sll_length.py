class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = last_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_node_after(self, prev, data):
        if not prev:
            print("Prev Node does not exist")
            return

        new_node = Node(data)

        new_node.next = prev.next
        prev.next = new_node

    def delete(self, key):
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = Node
            return

        prev = None

        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = Node

    def delete_by_pos(self, pos):
        curr_node = self.head

        if pos == 0:
            self.head = curr_node.next
            curr_node = Node
            return

        prev = None
        counter = 1
        if curr_node and counter != pos:
            prev = curr_node
            curr_node = curr_node.next
            counter += 1

        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = None

    def get_len(self):
        counter = 0
        curr_node = self.head

        # go through each Node until we hit none
        while curr_node:
            # keep count of the Nodes
            counter += 1
            curr_node = curr_node.next

        return counter

    def recursive_len(self, node):
        if node is None:
            return 0
        return 1 + self.recursive_len(node.next)


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")


print(llist.get_len())

sllist = LinkedList()
print("The length of an empty linked list is:")
print(llist.recursive_len(llist.head))
sllist.append("A")
sllist.append("B")
sllist.append("C")
sllist.append("D")

print("The length of the linked list calculated recursively after inserting 4 elements is:")
print(sllist.recursive_len(llist.head))
print("The length of the linked list calculated iteratively after inserting 4 elements is:")
print(sllist.get_len())
