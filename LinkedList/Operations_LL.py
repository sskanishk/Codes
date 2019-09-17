class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert the Node
    def insert(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    # Reverse the Linked List
    def reversess_list(self):
        if self.head is None:
            print("List is Empty")
            return
        else:
            prev = None
            temp = self.head
            while temp is not None:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            self.head = prev

    # Display List
    def viewList(self):
        if self.head is None:
            print("List is Empty")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

    # Delete the first node
    def delete_first_node(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            self.head = self.head.next

    # Delete the last Node
    def delete_last_node(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            temp = self.head
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = None

    # Count no. of nodes
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    # delete middle of the LinkedList
    def del_mid(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return None
        i = self.head
        j = self.head
        prev = None
        while (j != None and j.next != None):
            j = j.next.next
            prev = i
            i = i.next
        prev.next = i.next
        return

    # minNode() will find out the minimum value node in the list
    def minNode(self):
        temp = self.head
        if self.head is None:
            print("List is Empty")
        else:
            min = self.head.data
            while temp is not None:
                if min > temp.data:
                    min = temp.data
                temp = temp.next
            print(str(min))

    # maxNode() will find out the maximum value node in the list
    def maxNode(self):
        temp = self.head
        if self.head is None:
            print("list is empty")
        else:
            max = self.head.data
            while temp is not None:
                if max < temp.data:
                    max = temp.data
                temp = temp.next
            print(str(max))

    # remove duplicate
    def removeDup(self):
        curr = self.head
        index = None
        temp = None
        if self.head is None:
            print("list is empty")
        else:
            while curr is not None:
                temp = curr
                index = curr.next
                while index is not None:
                    if curr.data == index.data:
                        temp.next = index.next
                    else:
                        temp = index
                    index = index.next
                curr = curr.next

    # Sortting of daata in lInkedlist
    def sortt(self):
        curr = self.head
        index = None
        # temp = None
        if self.head is None:
            print("list is empty")
        else:
            while curr is not None:
                index = curr.next
                while index is not None:
                    if index.data < curr.data:
                        x = curr.data
                        curr.data = index.data
                        index.data = x
                    index = index.next
                curr = curr.next


mylst = LinkedList()
mylst.insert(1)
# mylst.insert(0)
# mylst.insert(2)
# mylst.insert(2)
# mylst.insert(0)
# mylst.insert(2)
# mylst.insert(1)
# mylst.insert(0)
# mylst.insert(2)
# mylst.insert(2)
# mylst.insert(0)
# mylst.insert(2)

print('list')
mylst.viewList()
print()

print('after delete_first_node')
mylst.delete_first_node()
mylst.viewList()
print()
#
# print('after delete_last_node')
# mylst.delete_last_node()
# mylst.viewList()
# print()
#
# print('No of nodes')
# print(mylst.count_nodes())
# # print()
#
# print('Reverse List')
# mylst.reversess_list()
# mylst.viewList()
# print()
#
# print('del med List')
# mylst.del_mid()
# mylst.viewList()
# print()
#
# print('Min node')
# mylst.minNode()
#
# print('Macx node')
# mylst.maxNode()
#
# print('delete Dup')
# mylst.removeDup()
# mylst.viewList()
# print()
#
# print('Sorting of data')
# mylst.sortt()
# mylst.viewList()
# print()