""" Structure of Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # Code here
        if head == None:
            return head
        prev=None
        while head:
            ne=head.next
            head.next=prev
            prev=head
            head=ne
        return prev
            