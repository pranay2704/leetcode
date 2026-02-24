# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head
        r1 = curr.next
        curr.next= r1.next
        r1.next=curr
        head=r1
        prev=curr
        curr=curr.next
        while curr is not None and curr.next is not None:
            r1=curr.next
            curr.next=r1.next
            r1.next=curr
            prev.next=r1

            prev=curr
            curr=curr.next
        return head

        return head
        
