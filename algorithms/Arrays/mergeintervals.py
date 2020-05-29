
from typing import List

class Solution:

    def merge_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda k:k[0])
        g_start, g_end = intervals[0]
        result = []
        for x in range(1, len(intervals)):
            interval = intervals[x]
            if g_end < interval[0]:
                result.append([g_start, g_end])
                g_start = interval[0]
                g_end = interval[1]
            else:
                g_end = max(g_end, interval[1])
        result.append([g_start, g_end])
        return result



print(Solution().merge_intervals([[1, 5], [2, 8], [10, 12]]))
# [[1, 8], [10, 12]]
            