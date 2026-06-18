class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        return min(abs((11*minutes - 60*(hour%12))/2), (360-abs((11*minutes - 60*(hour%12))/2)))
