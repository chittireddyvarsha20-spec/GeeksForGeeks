# Length of Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def getLength(self, head):
        # code here
        temp=head
        l=1
        while temp.next!=head:
            l+=1
            temp=temp.next
        return l
            
