class Solution:
    def reverseQueue(self, q):
        # code here
        z=deque([])
        while len(q)>0:
            z.append(q.pop())
        while len(z)>0:
            q.append(z.popleft())
