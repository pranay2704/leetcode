class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 1. Calculate the length of the list and find the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # 2. Optimize k: effectively, rotating length times returns the original list
        k = k % length
        if k == 0:
            return head
            
        # 3. Connect tail to head to make it a circular list
        tail.next = head
        
        # 4. Find the new tail: (length - k - 1) steps from head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        # 5. Break the circle and update the head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
