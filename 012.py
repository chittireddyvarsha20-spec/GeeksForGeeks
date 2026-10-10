# Check Linked List Is Sorted
''' Structure of linked list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def isSorted(self, head):
        # code here
        if head is None or head.next is None:
            return True
        temp=head
        while temp.next is not None and temp.data==temp.next.data:
            temp=temp.next
        if temp.next is None:
            return True
        if temp.data<temp.next.data:
            while temp.next!=None:
                if temp.data>temp.next.data:
                    return False
                temp=temp.next
        else:
            while temp.next!=None:
                if temp.data<temp.next.data:
                    return False
                temp=temp.next
        return True
