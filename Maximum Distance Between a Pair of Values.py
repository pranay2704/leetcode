class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        dist=0
        i=len(nums1)-1
        j=len(nums2)-1
        while i>-1:
            # print(nums1[i], nums2[0])
            if nums1[i]>nums2[0]:
                break
            while j>0 and j>=i and nums1[i]>nums2[j]:
                j-=1          
            if j!=-1:
                dist=max(dist,j-i)
            # print(i,j,dist)
            i-=1
        return dist
