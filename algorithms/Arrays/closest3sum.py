import collections

'''
This problem was recently asked by Google:

Given a list of numbers and a target number n, find 3 numbers combinatins in the list that sums closest to the target number n. There may be multiple ways of creating the sum closest to the target number, you can return any combination in any order.

Time: O(nlogn) + O(n2) = O(n2)
Space: O(n)

'''

class Solution:

    def closest_3_sum(self, nums, target):
        if not nums:
            return None
        distance = float("inf")
        res_set = collections.defaultdict(list)
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums)-1
            while j < k:
                cur_sum = nums[i]+nums[j]+nums[k]
                if abs(cur_sum-target) <= distance:
                    distance = abs(cur_sum-target)
                    res_set[distance].append([nums[i], nums[j], nums[k]])
                if cur_sum > target:
                    k -= 1
                else:
                    j += 1
        return distance, res_set.get(distance)



print(Solution().closest_3_sum([2, 1, -5, 4], -1))
# (1, [[-5, 1, 4], [-5, 1, 2]])