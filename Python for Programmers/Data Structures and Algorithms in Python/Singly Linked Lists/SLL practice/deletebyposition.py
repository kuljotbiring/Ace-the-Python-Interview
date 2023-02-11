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

        new_node.next = self.head.next
        self.head = new_node

    def insert_node_after(self, prev, data):
        if not prev:
            print("Prev does not exist")
            return

        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def delete_node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev = None

        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = None

    def delete_position(self, pos):
        # check if LL is empty
        if self.head:
            # curr Node initialized to head
            curr_node = self.head
            # if they wanted to delete head
            if pos == 0:
                # update head Node and delete curr Node
                self.head = curr_node.next
                curr_node = None
                return

            # save space for prev Node and set counter to zero
            prev = None
            count = 0

            # traverse the list while we are not at position
            while curr_node and count != pos:
                prev = curr_node
                curr_node = curr_node.next
                # update counter
                count += 1

            # if key did not match anything - exit
            if curr_node is None:
                return

            # update prev next point to following node and delete curr Node
            prev.next = curr_node.next
            curr_node = None

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.delete_node("B")
llist.delete_node("E")

llist.print_list()


