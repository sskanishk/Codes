class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = Node(value)
        else:
            new_node = Node(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = Node(value)
        else:
            new_node = Node(value)
            new_node.right_child = self.right_child
            self.right_child = new_node


def check_height(root):
    if root is None:
        return 0
    left_height = check_height(root.left_child)
    right_height = check_height(root.right_child)
    return max(left_height,right_height) + 1


def check_size(root):
    if root is None:
        return 0
    else:
        left_size = check_size(root.left_child)
        right_size = check_size(root.right_child)
        return left_size + right_size + 1


def diameter(root):
    if root is None:
        return 0

    left_height = check_height(root.left_child)
    right_height = check_height(root.right_child)

    left_dia = diameter(root.left_child)
    right_dia = diameter(root.right_child)
    return max(left_height + right_height + 1, max(left_dia, right_dia))


def inorder_print(root):
    if root.left_child is not None:
        inorder_print(root.left_child)
    print(root.value, end = " ")
    if root.right_child is not None:
        inorder_print(root.right_child)


def preorder_print(root):
    print(root.value, end=" ")
    if root.left_child is not None:
        preorder_print(root.left_child)
    if root.right_child is not None:
        preorder_print(root.right_child)


def postorder_print(root):
    if root.left_child is not None:
        postorder_print(root.left_child)
    if root.right_child is not None:
        postorder_print(root.right_child)
    print(root.value, end = " ")




a_node = Node(1)
a_node.insert_left(2)
a_node.insert_right(3)

b_node = a_node.left_child
b_node.insert_left(4)
b_node.insert_right(5)

c_node = a_node.right_child
c_node.insert_left(11)
c_node.insert_right(15)

d_node = c_node.right_child
d_node.insert_left(4)

e_node = d_node.left_child
e_node.insert_left(9)


print(diameter(a_node))

print(check_size(a_node))

# left -- root -- right
inorder_print(a_node)
print()

# root -- left -- right
preorder_print(a_node)
print()

# left -- right -- root
postorder_print(a_node)
