# Kth from End of Linked List
""" Structure of Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def getKthFromLast(self, head, k):
        # code here
        temp=head
        c=0
        while temp!=None:
            c+=1
            temp=temp.next
        if k>c or k<=0:
            return -1
        prev=None
        curr=head
        while curr!=None:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        temp=prev
        for i in range(k-1):
            temp=temp.next
        return temp.data
            
