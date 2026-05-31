class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        large = []
        for i in asteroids:
            if mass>=i:
                mass+=i
            else:
                heapq.heappush(large,i)
        while len(large)>0:
            k = heapq.heappop(large)
            if mass>=k:
                mass+=k
            else:
                return False
        return True
