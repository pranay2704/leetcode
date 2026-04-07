class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers)<3:
            return [1,2]
        for i in range(len(numbers)):
            low=i
            high=len(numbers)-1
            t2 = target-numbers[i]
            while low<=high:
                mid=low+((high-low+1)//2)
                print(numbers[i], numbers[mid], t2)
                if numbers[mid]==t2:
                    return [i+1,mid+1]
                elif numbers[mid]>t2:
                    high=mid-1
                else:
                    low=mid+1
        return [0,1]
