class MyLinkedList(object):

    def __init__(self):
        self.data = []

    def get(self, index):
        if index < 0 or index >= len(self.data):
            return -1
        return self.data[index]

    def addAtHead(self, val):
        self.data.insert(0, val)

    def addAtTail(self, val):
        self.data.append(val)

    def display(self):
        print(self.data)

    def addAtIndex(self, index, val):
        if index <= len(self.data):
            self.data.insert(index, val)

    def deleteAtIndex(self, index):
        if index >= 0 and index < len(self.data):
            self.data.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(2)
print(param_1)
obj.addAtHead(1)
obj.addAtHead(2)
obj.addAtHead(3)
obj.addAtHead(4)
obj.addAtHead(5)
print("Value for given index is", obj.get(2))
obj.display()
obj.addAtTail(8)
obj.display()
obj.addAtIndex(3,100)
obj.display()
param_1 = obj.get(2)
print(param_1)
# obj.deleteAtIndex(index)
