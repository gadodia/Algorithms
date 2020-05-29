'''
 This problem was recently asked by AirBNB:

Given a list of sorted numbers, and two integers k and x, find k closest numbers to the pivot x.

Time: O(logn) + O(n) = O(n)
Space: O(n)

'''

class Solution:

    def k_closest_elem(self, nums, k, x):
        if not nums:
            return None
        if x < nums[0]:
            return nums[:k]
        if x > nums[len(nums)-1]:
            return nums[::-k]
        left, right = self.pivot_loc(nums, x, 0, len(nums)-1)
        res = []
        while k > 0:
            while (left >= 0 and (x-nums[left]) <= (nums[right]-x)) and k > 0:
                res.append(nums[left])
                k -= 1
                left -= 1
            while (right < len(nums) and (nums[right]-x) <= (x-nums[left])) and k > 0:
                res.append(nums[right])
                k -= 1
                right += 1
            if left == 0 and k > 0:
                res += nums[right:k]
                k = 0
            if right == len(nums)-1 and k > 0:
                res += nums[left-k:left]
                k = 0
        return res

    def pivot_loc(self, nums, pivot, left, right):
        if left <= right:
            mid = left + (right-left)//2
            if nums[mid] >= pivot:
                if mid > 0 and nums[mid-1] <= pivot:
                    return mid-1, mid
                else:
                    return self.pivot_loc(nums, pivot, left, mid)
            if nums[mid] <= pivot:
                if mid < len(nums) and nums[mid+1] >= pivot:
                    return mid, mid+1
                else:
                    return self.pivot_loc(nums, pivot, mid, right)
        return None, None

print(Solution().k_closest_elem([1, 3, 7, 8, 9], 3, 5))
# [7, 3, 8]

print(Solution().k_closest_elem([1, 3, 7, 8, 9, 12, 15, 17, 19], 5, 11))
# [12, 9, 8, 7, 15]