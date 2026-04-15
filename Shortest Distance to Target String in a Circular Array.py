class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex]==target:
            return 0
        n = len(words)
        count=1
        left = (startIndex-1+n)%n
        right = (startIndex+1)%n
        while left!=right:
            if words[left]==target or words[right]==target:
                return count
            count+=1
            left = (startIndex-count+n)%n
            right = (startIndex+count)%n
            
        if words[left]==target or words[right]==target:
            return count
        return -1



