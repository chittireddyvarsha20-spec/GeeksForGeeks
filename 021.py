# Identical Linked List
'''
# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''
class Solution:
    def areIdentical(self, head1, head2):
        # Code here
        l1=[]
        l2=[]
        temp1=head1
        temp2=head2
        while temp1!=None:
            l1.append(temp1.data)
            temp1=temp1.next
        while temp2!=None:
            l2.append(temp2.data)
            temp2=temp2.next
        return len(l1)==len(l2) and l1==l2
        
        
