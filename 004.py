# Linked List End Insertion
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        newNode=Node(x)
        if head is None:
            return newNode
        newNode=Node(x)
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=newNode
        return head
            
