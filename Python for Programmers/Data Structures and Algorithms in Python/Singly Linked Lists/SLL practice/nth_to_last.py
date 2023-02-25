class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

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

    def insert_node_after(self, prev, data):
        if not prev:
            print("Prev Node does not exist")
            return

        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def delete_node(self, key):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return

        prev = None

        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if curr is None:
            return

        prev.next = curr.next
        curr = None

    def delete_by_pos(self, pos):
        if self.head:
            curr = self.head

            if pos == 0:
                self.head = curr.next
                curr = None
                return

            prev = None
            count = 1

            while curr and count != pos:
                prev = curr
                curr = curr.next
                count += 1

            if curr is None:
                return

            prev.next = curr.next
            curr = None

    def iterative_length(self):
        curr = self.head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        return count

    def recursive_length(self, node):
        if node is None:
            return 0

        return 1 + self.recursive_length(node.next)

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return

        prev_1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev_1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        if prev_1:
            prev_1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    def iterative_reverse(self):
        curr = self.head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def recursive_reverse(self):

        def _recursive_reverse(curr, prev):
            if not curr:
                return prev

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return _recursive_reverse(curr, prev)
        self.head = _recursive_reverse(curr=self.head, prev=None)

    def merge_sorted(self, llist):
        dummy = Node(0)
        tail = dummy
        list1 = self.head
        list2 = llist.head

        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

    def nth_to_last(self, n):
        list_length = self.iterative_length()

        curr = self.head

        while curr and list_length != n:
            list_length -= 1
            curr = curr.next

        if curr is None:
            return
        else:
            return curr.data


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print(llist.nth_to_last(2))




