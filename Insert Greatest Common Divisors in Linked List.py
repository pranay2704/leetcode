# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def GCD(self, a, b):
        if a%b == 0:
            return b
        return self.GCD(b,a%b)
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = prev.next
        while curr is not None:
            Node = ListNode(self.GCD(prev.val,curr.val), curr)
            prev.next = Node
            #shift Node
            prev = curr
            curr = curr.next
        return head



        
