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

    def len_iterative(self):
        curr_node = self.head
        counter = 0
        if curr_node:
            counter += 1
            curr_node = curr_node.next

        return counter

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_node(self, key_1, key_2):
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

        if not curr_1 or not  curr_2:
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
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                return _reverse_recursive(curr, prev)
        self.head = _reverse_recursive(curr=self.head, prev=None)

    # pass in llist which is second linked list we are going to merge
    def merge_sorted(self, llist):
        # point to the heads of each LL
        p = self.head
        q = llist.head
        s = None

        # handle cases if LL is empty
        if not p:
            return q
        if not q:
            return p

        # if both heads exist then compare data of nodes they are pointing to
        if p and q:
            # if value in p is less than value in q
            if p.data <= q.data:
                # s point to p
                s = p
                # p moves along if s points to node it was previously pointing to
                p = s.next
            # value in q is less than value in p
            else:
                # s points to q
                s = q
                # p moves along if s points to node it was previously pointing to
                q = s.next
            # whichever was one was lower, set it to the new head
            new_head = s
        # run until finished with either LL
        while p and q:
            # if value in p is less than value in q
            if p.data <= q.data:
                # save what p is pointing to
                s.next = p
                # update value of s to p because p.data was less than q.data
                s = p
                # make p move by pointing it to the next node of s
                p = s.next
            # value in q is less than value in p
            else:
                # save what q is pointing to
                s.next = q
                # update value of s to q because p.data was less than p.data
                s = q
                # make q move by pointing it to the next node of s
                q = s.next
        # we have reached the end of either LL
        # find out which LL we have reached the end of
        # if we reached end of p
        if not p:
            # s will now point to the remaining llist
            s.next = q
        # if we reached end of p
        if not q:
            # s will now point to the remaining llist
            s.next = p
        # return head node of merged LL
        self.head = new_head
        return self.head
