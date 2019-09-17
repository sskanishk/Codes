class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Dub_LL:
    def __init__(self):
        self.head = None

    def insert_append(self, value):
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

    def reverse(self):
        if self.head is None:
            return f"List is Empty"
        curr = self.head
        temp = curr.next
        curr.next = None
        curr.prev = temp
        while temp is not None:
            temp.prev = temp.next
            temp.next = curr
            curr = temp
            temp = temp.prev
        self.head = curr



    def Display(self):
        if self.head is None:
            return f"List is empty"
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next



dll = Dub_LL()
dll.insert_append(1)
dll.insert_append(2)
dll.insert_append(3)
dll.insert_append(4)
dll.insert_append(5)

dll.Display()
print()
dll.reverse()
dll.Display()

