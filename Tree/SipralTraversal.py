# Spiral / ZigZag Traversal fo Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def zizagtraversal(root):
	if root is None:
		return

	s1 = []
	s2 = []

	# l - t - r
	# if temp is true
	# push node from left to right
	# otherwise right to left
	ltr = True

	s1.append(root)

	while len(s1) > 0:
		temp = s1.pop(-1)
		print(temp.value, end = " ")

		if ltr:
			if temp.left:
				s2.append(temp.left)
			if temp.right:
				s2.append(temp.right)

		else:
			if temp.right:
				s2.append(temp.right)
			if temp.left:
				s2.append(temp.left)

		if len(s1) == 0:
			ltr = not ltr
            # swap the stack
			s1, s2 = s2, s1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("Zigzag Order traversal of binary tree is")
zizagtraversal(root)



