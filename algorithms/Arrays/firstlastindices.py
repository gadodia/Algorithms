'''
This problem was recently asked by AirBNB:

Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
'''

class Solution: 
    def getRange(self, arr, target):
        first_index = self.getRangeHelper(arr, 0, len(arr), target, 'first')
        last_index = self.getRangeHelper(arr, 0, len(arr), target, 'last')
        return [first_index, last_index]

    def getRangeHelper(self, arr, low, high, target, index_type):
        if low <= high:
            mid = low + (high - low)//2
            if arr[mid] < target:
                return self.getRangeHelper(arr, mid+1, high, target, index_type)
            elif arr[mid] > target:
                return self.getRangeHelper(arr, low, mid-1, target, index_type)
            else:
                if index_type == 'first':
                    if mid > 0 and arr[mid-1] == target:
                        return self.getRangeHelper(arr, low, mid-1, target, index_type)
                else:
                    if mid < len(arr)-1 and arr[mid+1] == target:
                        return self.getRangeHelper(arr, mid+1, high, target, index_type)
                return mid
        return -1 
    
  

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

arr = [1,3,3,5,7,8,9,9,9,15]
x = 9
print(Solution().getRange(arr, x))
# [6, 8]

arr = [100, 150, 150, 153]
x = 150
print(Solution().getRange(arr, x))
# [1, 2]

arr = [1,2,3,4,5,6,10]
x = 9
print(Solution().getRange(arr, x))
# [-1 ,-1]