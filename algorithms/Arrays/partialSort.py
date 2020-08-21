'''
This problem was recently asked by Uber:

You are given a list of n numbers, where every number is at most k indexes away from its properly sorted index. Write a sorting algorithm (that will be given the number k) for this list that can solve this in O(n log k)

Example:
Input: [3, 2, 6, 5, 4], k=2
Output: [2, 3, 4, 5, 6]
As seen above, every number is at most 2 indexes away from its proper sorted index.

Time: O(nlogk)
Space: O(k)
'''
import heapq

class Solution:

    def sort_partially_sorted(self, nums, k):
        heap = []
        heap += nums[:k+1]
        heapq.heapify(heap)
        j = 0
        for i in range(len(nums)):
            nums[j] = heapq.heappop(heap)
            if i+k+1 < len(nums):
                heapq.heappush(heap, nums[i+k+1])
            j += 1
        return nums


print(Solution().sort_partially_sorted([3, 2, 6, 5, 4], 2))
# [2, 3, 4, 5, 6]