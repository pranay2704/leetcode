class Solution:    
    def rotateDeque(self, dq, type, k):
        #code here
        # if type==1:
        #     while k>0:
        #         i=dq.pop()
        #         dq.appendleft(i)
        #         k-=1
        # else:
        #     while k>0:
        #         i=dq.popleft()
        #         dq.append(i)
        #         k-=1
        if type==1:
            dq.rotate(k)
        else:
            dq.rotate(-k)
        
