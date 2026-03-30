# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = ListNode()
        res = [None for _ in range(k) ]
        curr=head
        total = 0
        while curr!=None:
            total+=1
            curr = curr.next
        part = total//k
        remainder = total%k
        curr=head
        print(part," ",remainder)
        i=0
        if part==0:
            while curr!=None:
                curr1 = curr
                curr = curr.next
                curr1.next=None
                res[i] = curr1
                i+=1
        else:
            while curr!=None:
                head1 = curr
                curr1 = head1
                j=0
                part1 = part
                if i>=remainder:
                    part1=part-1
                print(part1)
                while curr1.next!=None and  j<part1:
                    curr1=curr1.next
                    j+=1
                curr = curr1.next
                curr1.next=None
                res[i] = head1
                i+=1

        return res

