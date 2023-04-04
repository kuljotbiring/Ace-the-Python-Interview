class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start, traversal):
        """
        Check if the current node is empty/null.
        Display the data part of the root (or current node).
        Traverse the left subtree by recursively calling the pre-order method.
        Traverse the right subtree by recursively calling the pre-order method.
        """
        # Root->Left->Right
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """
        Check if the current node is empty/null.
        Traverse the left subtree by recursively calling the in-order method.
        Display the data part of the root (or current node).
        Traverse the right subtree by recursively calling the in-order method.
        """
        # Left->Root->Right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)