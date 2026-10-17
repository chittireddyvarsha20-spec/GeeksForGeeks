#insert at middle of Linked list 
'''
structure of a linked list node 
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def insertInMiddle(self, head, x):
        #code here
        nn=Node(x)
        if head==None:
            return nn
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        nn.next=slow.next
        slow.next=nn
        return head
