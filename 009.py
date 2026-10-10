# Node At Given Index
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''


class Solution:

    def getNode(self, head: 'Node', k: int) -> int:
        """ code here """
        count=0
        temp=head
        while temp!=None:
            count+=1
            temp=temp.next
        if k>count:
            return -1
        temp=head
        while k-1:
            temp=temp.next
            k-=1
        return temp.data
