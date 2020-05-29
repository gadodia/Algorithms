from heapq import heapify, heappop, heappush
import collections

'''
Time: O(n) + O(nlogk)
Space: O(n)
'''
class Solution:


    def __init__(self, nums, k):
        self.heap = []
        self.k = k
        self.nums = nums
    
    def topk(self):
        freq = collections.defaultdict(int)
        for num in self.nums:
            freq[num] += 1
        print(freq)
        for key, val in freq.items():
            heappush(self.heap, (val, key))
            if len(self.heap) > self.k:
                heappop(self.heap)            
        return [x[1] for x in self.heap]


if __name__ == '__main__':
    s = Solution([1,1,2,2,2,2,5,5,5,5,5,5,3,3,3], 2) 
    print(s.topk())

