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

    def Remove_Node(self, key):
        temp = self.head
        if self.head.data is key:
            while temp.next is not self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
        # else:
        #     while temp.next.data is not key:
        #         temp = temp.next
        #     temp.next = temp.next.next
        else:
            prev = None
            while temp.next is not self.head:
                prev = temp
                temp = temp.next
                if temp.data is key:
                    prev.next = temp.next
                    temp = temp.next





CLL = CircularLinkedList()
CLL.Append(1)
CLL.Append(2)
CLL.Append(3)
CLL.Append(4)
CLL.Append(5)
CLL.Append(6)
CLL.Append(7)

CLL.Display()
print()
CLL.Remove_Node(1)
CLL.Remove_Node(2)
CLL.Remove_Node(3)
CLL.Remove_Node(5)
CLL.Remove_Node(6)
CLL.Remove_Node(7)



CLL.Display()


