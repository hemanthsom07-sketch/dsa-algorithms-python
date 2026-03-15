# Inorder Traversal using user input (Binary Search Tree)

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


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# User input
values = input("Enter numbers separated by space: ").split()
values = list(map(int, values))

root = None

for v in values:
    root = insert(root, v)

print("Inorder Traversal:")
inorder(root)
