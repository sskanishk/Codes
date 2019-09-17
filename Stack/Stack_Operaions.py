class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def Display(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
'''
s = Stack()
s.push(1)
s.push(2)
print(s.Display())
s.push(3)
s.push(4)
print(s.Display())
s.pop()
s.push(5)
print(s.Display())
s.pop()
print(s.Display())
# s.pop()
# s.pop()
# s.pop()
print(s.Display())

print("calling is_empty function = ",s.is_empty())
print(s.peek())
'''
# in stack top element is cosnider as last element.. i.e. [-1] last element