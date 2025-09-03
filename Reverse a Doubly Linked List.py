"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        reverse = Node(None)
        reverse.data=head.data
        while(1):
            if head.next==None:
                break
            head=head.next
            new = Node(None)
            new.data=head.data
            
            reverse.prev=new
            new.next=reverse
            reverse=reverse.prev
        return reverse
        
        
