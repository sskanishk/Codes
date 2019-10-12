# Linkedlist Comparison

def compare_lists(llist1, llist2):
    if (llist1 == None and llist2 == None):
        return 1
    else:
        if (llist1 == None or llist2 == None):
            return 0

    if (llist1.data == llist2.data):
        return compare_lists(llist1.next, llist2.next)
    else:
        return 0


# merging of two sorted linkedlist

def mergeLists(head1, head2):
    if head1 == None and head2 == None:
        return None
    if head1 != None and head2 == None:
        return head1
    if head1 == None and head2 != None:
        return head2

    if head1.data < head2.data:
        smallerNode = head1
        smallerNode.next = mergeLists(head1.next, head2)
    else:
        smallerNode = head2
        smallerNode.next = mergeLists(head1, head2.next)

    return smallerNode


