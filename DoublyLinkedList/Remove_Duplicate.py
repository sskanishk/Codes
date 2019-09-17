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

    def Remove_duplicate(self):
        temp = self.head
        seen = dict()
        while temp is not None:
            if temp.data not in seen:
                seen[temp.data] = 1
                temp = temp.next
            else:
                nxt = temp.next
                # delete is another function used in remove duplicates
                self.deletex(temp)
                temp = nxt

    def deletex(self, node):
        temp = self.head
        while temp:
            # change key to node
            if temp is node and temp is self.head:
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

            # change key to node
            elif temp is node:
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
dll.insert_append(4)
dll.insert_append(4)
dll.insert_append(5)

dll.Display()
print()
dll.Remove_duplicate()
dll.Display()

