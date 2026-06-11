"""
Approach:
1. Could sort the list
   points.sort(key = lambda x : (x ** 2 + x ** 2) ** 0.5)
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point : (point[0] ** 2 + point[1] ** 2) ** 0.5)
        return points[:k]