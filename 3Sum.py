class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
        print(nums)
        res=[]
        for i in range(1,len(nums)-1):
            p1=0
            p2=len(nums)-1
            while p1<i and i<p2:
                t=nums[p1]+nums[i]+nums[p2]
                if t==0:
                    if [nums[p1], nums[i], nums[p2]] not in res:
                        res.append([nums[p1], nums[i], nums[p2]])
                    p1+=1
                    p2-=1
                elif t>0:
                    p2-=1
                else:
                    p1+=1
        return res
