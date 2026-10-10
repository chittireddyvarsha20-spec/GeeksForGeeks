# Insertion IN Empty Circular Linked List
""" Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Initially, the next pointer is None.
 """ 
class Solution:
    def insertIntoEmpty(self, last, data):
        # code here
        newnode=Node(data)
        newnode.next=newnode
        return newnode
