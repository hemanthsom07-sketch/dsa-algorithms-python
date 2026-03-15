# Preorder Traversal with User Input

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# User input
values = list(map(int, input("Enter node values separated by space: ").split()))

root = None
for v in values:
    root = insert(root, v)

print("Preorder Traversal:")
preorder(root)
