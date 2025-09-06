class Solution:
    def lengthOfLoop(self, head):
        #code here
        nodes={}
        while head not in nodes:
            if head is None:
                return 0
            for i in nodes:
                nodes[i]+=1
                # if nodes[i]>max:
                #     max=nodes[i]
            nodes[head]=1
            head=head.next
        return nodes[head]
