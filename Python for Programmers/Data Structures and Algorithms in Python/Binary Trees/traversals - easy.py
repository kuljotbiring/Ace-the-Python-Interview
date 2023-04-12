class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root):
    # left -> root -> right
    if root:
        # first recursive call on left child
        inorder_traversal(root.left)
        # then print the data of the node
        print(root.val)
        # now recur on right child
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root:
        # first print the data of the node
        print(root.val)
        # then recursive call on left child
        preorder_traversal(root.left)
        # finally, recursive call on right child
        preorder_traversal(root.right)


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)