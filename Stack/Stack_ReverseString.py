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

    # Shortcut Method to Reverse string
    def x(self):
        print("Hello"[::-1])

    def Reverse_String(self, s, input_str):
        for i in range(len(input_str)):
            s.push(input_str[i])
        rev_str = ""
        while not s.is_empty():
            rev_str += s.pop()
        return rev_str


s = Stack()
input_str = "REVERSE"
print(s.Reverse_String(s, input_str))