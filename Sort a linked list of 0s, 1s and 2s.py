'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        prev=head
        curr=head.next
        nex=head.next.next
        head.next=curr
        curr.next=head
        # head_1=head
        # while head:
        #     while head.data>head.next.data:
        #         curr=head
        #         head=head.next
        #         head.next=curr
        
        return head
                
