# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
#         return points[:k]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lt = []
        for i in points:
            k1 = sqrt(i[0]**2+i[1]**2)
            if len(lt)<k:
                heapq.heappush(lt, (-k1,i))
            else:
                heapq.heappushpop(lt, (-k1,i))
        # q = heapq.nsmallest(k,lt)
        q = [i[1] for i in lt]
        return q
