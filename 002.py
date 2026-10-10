#Print Linked List
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def printList(self, head):
        # code here
        res=[]
        while head is not None:
            res.append(head.data)
            head=head.next
        return res
