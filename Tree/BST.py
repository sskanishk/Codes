class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# function to insert a new node with the given value
def insert(root, node):
    if root is None:
        root = Node
    else:
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inorder_print_bst(root):
    if root.left is not None:
        inorder_print_bst(root.left)
    print(root.value, end=" ")
    if root.right is not None:
        inorder_print_bst(root.right)

def postorder_print_bst(root):
    if root.left is not None:
        postorder_print_bst(root.left)
    if root.right is not None:
        postorder_print_bst(root.right)
    print(root.value, end=" ")

def preorder_print_bst(root):
    print(root.value, end=" ")
    if root.left is not None:
        preorder_print_bst(root.left)
    if root.right is not None:
        preorder_print_bst(root.right)



root = Node(50)
insert(root, Node(20))
insert(root, Node(70))
insert(root, Node(10))
insert(root, Node(30))
insert(root, Node(60))
insert(root, Node(90))

inorder_print_bst(root)
print()
preorder_print_bst(root)
print()
postorder_print_bst(root)


