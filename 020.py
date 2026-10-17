# Palindrome Linked List
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        l=[]
        temp=head
        while temp!=None:
            l.append(temp.data)
            temp=temp.next
        r=[]
        prev=None
        curr=head
        while curr!=None:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        while prev is not None:
            r.append(prev.data)
            prev=prev.next
        return l==r
        
        
           
