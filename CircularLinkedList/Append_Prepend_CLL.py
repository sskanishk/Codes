class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def Append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head

    def Prepend(self, data):
        newNode = Node(data)
        temp = self.head
        newNode.next = self.head

        if not self.head:
            newNode.next = newNode
        else:
            while temp.next is not self.head:
                temp = temp.next
            temp.next = newNode
        self.head = newNode

    def Display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end =" ")
            temp = temp.next
            if temp is self.head:
                break


CLL = CircularLinkedList()
# CLL.Append(1)
# CLL.Append(2)
# CLL.Append(3)
# CLL.Append(4)
# CLL.Append(5)
# CLL.Append(6)
# CLL.Append(7)

CLL.Prepend(1)
CLL.Prepend(2)
CLL.Prepend(3)
CLL.Prepend(4)
CLL.Prepend(5)
CLL.Prepend(6)
CLL.Prepend(7)

CLL.Display()



