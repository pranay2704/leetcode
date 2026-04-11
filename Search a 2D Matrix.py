class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, low1 = 0,0
        high, high1 = len(matrix)-1, len(matrix[0])-1

        while low<=high:
            mid = (low+high)//2
            print(mid)
            if matrix[mid][-1]==target:
                return True
            elif matrix[mid][-1]<target:
                low = mid+1
            else:
                if matrix[mid][0]>target:
                    high=mid-1
                elif target in matrix[mid]:
                    return True
                else:
                    return False
        return False




