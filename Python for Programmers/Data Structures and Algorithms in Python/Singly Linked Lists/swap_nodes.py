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
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Prev node does not exist")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

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

    def delete_by_pos(self, pos):
        curr_node = self.head

        if pos == 0:
            self.head = curr_node.next
            curr_node = None
            return

        prev = None
        count = 1

        while curr_node and count != pos:
            prev = curr_node
            curr_node = curr_node.next
            count += 1

        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = None

    def get_length(self):
        curr_node = self.head
        counter = 0

        while curr_node:
            counter += 1
            curr_node = curr_node.next

        return counter

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        # check if both keys are the same element - nothing to swap!
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        # loop through the linked list while curr_1 is not at end of LL
        # or is it not equal to the key_1 that we are looking for
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        # loop through the linked list while curr_2 is not at end of LL
        # or is it not equal to the key_2 that we are looking for
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        # check if the elements exist or not
        if not curr_1 or not curr_2:
            return

        # if previous node exists, then curr Node is not a head Node
        if prev_1:
            # if prev existed then swap it
            prev_1.next = curr_2
        # otherwise, it was a head Node, and we set the head to its new value
        else:
            self.head = curr_2

        # if previous node exists, then curr Node is not a head Node
        if prev_2:
            # if prev existed then swap it
            prev_2.next = curr_1
        # otherwise, it was a head Node, and we set the head to its new value
        else:
            self.head = curr_1

        # swap what the curr Node next was pointing to
        curr_1.next, curr_2.next = curr_2.next, curr_1.next


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print("Original List")
llist.print_list()


llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print_list()

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node")
llist.print_list()

llist.swap_nodes("D", "B")
print("Swapping nodes D and B where key_2 is head node")
llist.print_list()

llist.swap_nodes("C", "C")
print("Swapping nodes C and C where both keys are same")
llist.print_list()
