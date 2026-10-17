# Insert In Sorted List
'''Definition of a Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''

class Solution:
    def sortedInsert(self, head, key):
        # code here
        temp=head
        prev=None
        while temp!=None:
            if key<=temp.data:
                nn=Node(key)
                if head==temp:
                    nn.next=head
                    head=nn
                    return head
                prev.next=nn
                nn.next=temp
                return head
            prev=temp
            temp=temp.next
        nn=Node(key)
        prev.next=nn
        return head
            
