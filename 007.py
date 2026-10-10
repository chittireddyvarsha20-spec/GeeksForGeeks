# Linked List Traversal
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def printList(self, head):
        res=[]
        # code here
        while head is not None:
            print(head.data,end=" ")
            head=head.next
