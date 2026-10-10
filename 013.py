# Sum of Last n Nodes of a Linked List
''' Structure for link list Node
    class Node:
        def __init__(self, val):
            self.data = val
            self.next = None
'''

class Solution:
    def sumofNodes(self, head, n):
        # code here
        c=0
        temp=head
        while temp!=None:
            c+=1
            temp=temp.next
        k=c-n
        sum=0
        i=0
        temp=head
        while i<k:
            temp=temp.next
            i+=1
        while temp is not None:
            sum+=temp.data
            temp=temp.next
        return sum
            
