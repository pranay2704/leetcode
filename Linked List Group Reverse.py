"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        main_head=head
        # while head is not None:
        #     res = []
        #     i=0
        #     head_temp=head
        #     while i<k:
        #         if head is not None:
        #             res.append(head.data)
        #             head=head.next
        #             i+=1
        #         else:
        #             break
            
        #     while not bool(res):
        #         head_temp.data=res.pop()
        #         head_temp=head_temp.next
        lt = []
        lt.append(1)
        lt.append(2)
        print(lt)
        # while not bool(lt):
        #     lt.pop()
        return main_head
