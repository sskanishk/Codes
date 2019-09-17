class Stack():
    """ this constructor function going to modify the python list"""

    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

    def Sol(self, dec_no):
        # s = Stack()
        while dec_no > 0:
            remainder = dec_no % 2
            s.push(remainder)
            dec_no = dec_no // 2

        bin_no = ""
        while not s.is_empty():
            bin_no += str(s.pop())

        return(bin_no)


s = Stack()
# return in def
# s.Sol(242)
# print in def
print(s.Sol(141))

