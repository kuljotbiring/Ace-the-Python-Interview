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

    def insert_after_node(self, prev, data):
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

        prev = None
        counter = 1
        while curr_node and counter != pos:
            prev = curr_node
            curr_node = curr_node.next
            counter += 1

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

    def get_length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.get_length_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 and not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        curr_node = self.head
        # run until curr_node is not equal to None
        while curr_node:
            # next_node is used as temporary value to store curr_node.next
            next_node = curr_node.next
            # curr_node.next gets modified to flip the arrows
            # instead of pointing to next Node, we point to next of the current node
            # to the previous Node
            curr_node.next = prev
            # iterate through LL while keeping track of previous and current Nodes
            prev = curr_node
            curr_node = next_node
        # after iterating through LL, prev is last Node in LL
        # set self.head equal to last Node of LL
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(curr, prev):
            # base case. activated when reaching end of LL
            if not curr:
                return prev
            # store the next node in a temporary variable
            nxt = curr.next
            # make the next pointer point to previous node
            curr.next = prev
            # update the previous node to the current node
            prev = curr
            # update the current node to the node we saved earlier
            curr = nxt
            # recursive function call
            return _reverse_recursive(curr, prev)

        self.head = _reverse_recursive(curr=self.head, prev=None)


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print("Print the Linked List")
llist.print_list()

llist.reverse_iterative()

print("\nPrint the Linked List reversed iteratively")
llist.print_list()

llist.reverse_recursive()

print("\nPrint the Linked List reversed recursively")
llist.print_list()
