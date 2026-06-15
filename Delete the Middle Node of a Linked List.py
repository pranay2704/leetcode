class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node1 = head
        node2 = head

        if node2.next==None:
            return None
        elif node2.next.next==None:
            node1.next=None
            return head         
        node2=node2.next.next
        while node2.next!=None:
            node1=node1.next
            if node2.next.next!=None:
                node2=node2.next.next
            else:
                node2=node2.next
        node1.next=node1.next.next
        return head

        
