# Join To Linked Lists
''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def joinLists(self, head1, head2):
       # code here
        temp=head1
        while temp.next!=None:
           temp=temp.next
        temp.next=head2
        return head1
        
