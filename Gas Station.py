total = 0
        curr = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            curr += diff
            if curr < 0:
                start = i + 1
                curr = 0
        return start if total >= 0 else -1

class Solution:
#     def startStation(self, gas, cost):
#         #  code here
#         temp=[]
#         k=[]
#         total=0
#         if len(gas)==1 and cost[0]<=gas[0]:
#             return 0
#         for i in range(len(gas)):
#             z=gas[i]-cost[i]
#             temp.append(z)
#             total+=z
#             if z>0:
#                 k.append(i)
#         if total<0:
#             return -1
#         # print(temp)
#         total=0
#         for i in k:
#             start=i
#             total=0
#             while start<len(temp) and total>=0:
#                 # print(total,'-',temp[start],'-',start)
#                 total+=temp[start]
#                 start+=1
#             start=0
#             # print(total,'-',i)
#             if total<0:
#                 continue
#             while start<i and total>0:
#                 total+=temp[start]
#                 start+=1
#             # print(total,'-',i)
#             if total<0:
#                 continue
#             else:
#                 return i
            
