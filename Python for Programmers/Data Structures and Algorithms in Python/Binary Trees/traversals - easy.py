class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root):
    """When using BST and inorder traversal, we can get nodes in non-decreasing order
    Time complexity: O(n). Space complexity: O(1)"""
    # left -> root -> right
    if root:
        # first recursive call on left child
        inorder_traversal(root.left)
        # then print the data of the node
        print(root.val)
        # now recur on right child
        inorder_traversal(root.right)


def preorder_traversal(root):
    """Preorder used to create copy of the tree. Also used to get prefix expressions on expression tree
    Time complexity: O(n). Space complexity: O(1)"""
    # root -> left -> right
    if root:
        # first print the data of the node
        print(root.val)
        # then recursive call on left child
        preorder_traversal(root.left)
        # finally, recursive call on right child
        preorder_traversal(root.right)


def postorder_traversal(root):
    """Postorder used to delete a tree. Also useful to get postfix expression of expression tree
    Time complexity: O(n). Space complexity: O(1)"""
    if root:
        # left -> right -> root
        # first recursive call on left child
        postorder_traversal(root.left)
        # then recursive call on right child
        postorder_traversal(root.right)
        # finally, print the data of the node
        print(root.val)


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal: ")
    inorder_traversal(root)
    print("\n")
    print("Preorder traversal: ")
    preorder_traversal(root)
    print("\n")
    print("Postorder traversal: ")
    postorder_traversal(root)
