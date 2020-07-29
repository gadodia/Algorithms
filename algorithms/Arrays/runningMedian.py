'''
This problem was recently asked by Google:

You are given a stream of numbers. Compute the median for each new element .

Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]

Time: O(n)
Space: O(n)
'''
from typing import List
import heapq

class Solution:

    def running_median(self, stream: List[int]) -> List[int]:
        heapl, heapr = [], []
        res = []
        for num in stream:
            heapq.heappush(heapl, num)
            if len(heapl)-len(heapr) > 1:
                heapq.heappush(heapr, -(heapq.heappop(heapl)))
            if len(heapl) > len(heapr):
                res.append(heapl[0])
            else:
                res.append((heapl[0]-heapr[0])/2)
        return res


print(Solution().running_median([2, 1, 4, 7, 2, 0, 5]))
# 2 1.5 2 3.0 2 2.0 2
