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

    def insert_node_after(self, prev, data):
        if not prev:
            print("Prev node does not exist")
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

    def delete_by_pos(self, pos):
        if self.head:
            curr_node = self.head

            if pos == 0:
                self.head = curr_node.next
                curr_node = None
                return

            prev = 0
            count = 1

            while curr_node and count != pos:
                prev = curr_node
                curr_node = curr_node.next
                count += 1

            if curr_node is None:
                return

            prev.next = curr_node.next
            curr_node = None

    def length_iterative(self):
        curr_node = self.head
        count = 0

        while curr_node:
            count += 1
            curr_node = curr_node.next

        return count

    def length_recursive(self, node):
        if node is None:
            return 0

        return 1 + self.length_recursive(node.next)

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
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

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(curr, prev):
            if not curr:
                return prev

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return _reverse_recursive(curr, prev)
        self.head = _reverse_recursive(curr=self.head, prev=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

            if not p:
                s.next = q
            if not q:
                s.next = p
            return new_head

    def remove_duplicates(self):
        curr = self.head
        prev = None
        dup_values = dict()

        while curr:
            if curr.data in dup_values:
                # remove Node
                prev.next = curr.next
                curr = None
            else:
                # have not encountered element before
                dup_values[curr.data] = 1
                prev = curr
            curr = prev.next

