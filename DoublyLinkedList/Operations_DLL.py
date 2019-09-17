class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DubLinkedList:
	def __init__(self):
		self.head = None

	# inseting the node after node
	def insert_next_append(self, value):
		newNode = Node(value)
		if self.head is None:
			self.head = newNode
			newNode.prev = None
		else:
			temp = self.head
			while temp.next is not None:
				temp = temp.next
			temp.next = newNode
			newNode.next = None
			newNode.prev = temp

	# inseting the node before node
	def insert_prev_prepend(self, value):
		newNode = Node(value)
		if self.head is None:
			self.head = newNode
			newNode.prev = None
		else:
			temp = self.head
			temp.prev = newNode
			newNode.next = self.head
			self.head = newNode
			newNode.prev = None


	# inserting node after defined key in list
	def insert_after_def_node(self, key, value):
		temp = self.head
		newNode = Node(value)
		while temp:
			if temp.next is None and temp.data is key:
				self.insert_next_append(value)
				return
			elif temp.data is key:
				next = temp.next
				temp.next = newNode
				newNode.next = next
				newNode.prev = temp
				next.prev = newNode
			temp = temp.next

	# inserting node after defined key in list
	def insert_before_def_node(self, key, value):
		temp = self.head
		newNode = Node(value)
		while temp:
			if temp.prev is None and temp.data is key:
				self.insert_prev_prepend(value)
				return
			elif temp.data is key:
				prev = temp.prev
				temp.prev = newNode
				newNode.next = temp
				newNode.prev = prev
				prev.next = newNode
			temp = temp.next

	# Delete Operations
	def Delete_node(self, key):
		temp = self.head
		while temp:
			if temp.data is key and temp is self.head:
				# only one node in list to delete  --- working
				if not temp.next:
					temp = None
					self.head = None
					return
				# multiple node and delete head node  --- working
				else:
					next = temp.next
					temp.next = None
					next.prev = None
					temp = None
					self.head = next
					return

			elif temp.data is key:
				# delete the node in between except head and tail -- working
				if temp.next:
					prev = temp.prev
					next = temp.next
					next.prev = temp.prev
					prev.next = temp.next
					temp.next = None
					temp.prev = None
					temp = None
					return

				# last node having next is none -- working
				else:
					prev = temp.prev
					prev.next = temp.next
					temp.prev = None
					temp.next = None
					temp = None
					return
			temp = temp.next

	def DisplayList(self):
		if self.head is None:
			print("List is Empty")
			return
		else:
			temp = self.head
			while temp is not None:
				print(temp.data, end=" ")
				temp = temp.next

dll = DubLinkedList()
# dll.insert_prev_prepend(1)
# dll.insert_prev_prepend(2)
# dll.insert_prev_prepend(3)
# dll.insert_prev_prepend(4)
# dll.insert_prev_prepend(5)
# dll.insert_prev_prepend(6)
# dll.insert_prev_prepend(7)
# dll.insert_prev_prepend(8)

dll.insert_next_append(1)
dll.insert_next_append(2)
dll.insert_next_append(3)
dll.insert_next_append(4)
dll.insert_next_append(5)
dll.insert_next_append(6)
dll.insert_next_append(7)
dll.insert_next_append(8)

dll.DisplayList()
print()

# inserting node after the key 3
dll.insert_after_def_node(3, 656)
dll.DisplayList()
print()

# inserting node before the key 7
dll.insert_before_def_node(7, 656)
dll.DisplayList()
print()


dll.Delete_node(8)
dll.Delete_node(3)
dll.Delete_node(1)
dll.DisplayList()