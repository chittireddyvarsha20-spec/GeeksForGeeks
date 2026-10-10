# Length of Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def getCount(self, head):
        # code here
        count=0
        while head is not None:
            count+=1
            head=head.next
        return count
        
