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

    def __len__(self):
        temp = self.head
        count = 0
        while temp.next is not self.head:
            count += 1
            temp = temp.next
            if temp is self.head:
                break
        return count

    def split_list(self):
        size = len(self)
        if size is 0:
            return None
        if size is 1:
            return self.head
        count = 0
        mid = size//2
        prev = None
        temp = self.head
        while temp and count < mid:
            count += 1
            prev = temp
            temp = temp.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while temp.next is not self.head:
            split_cllist.append(temp.data)
            temp = temp.next
        split_cllist.append(temp.data)
        self.Display()
        print('\n')
        split_cllist.Display()










CLL = CircularLinkedList()
CLL.Append(1)
CLL.Append(2)
CLL.Append(3)
CLL.Append(4)
CLL.Append(5)
CLL.Append(6)
# CLL.Append(7)

CLL.Display()
print()


CLL.split_list()

CLL.Display()


