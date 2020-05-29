'''
This problem was recently asked by Apple:

The Fibonacci sequence is the integer sequence defined by the recurrence relation: F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. In other words, the nth Fibonacci number is the sum of the prior two Fibonacci numbers. Below are the first few values of the sequence:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

Given a number n, print the n-th Fibonacci Number.
Examples:
Input: n = 3
Output: 2

Input: n = 7
Output: 13
'''

class Solution:

    def Fibonacci(self, n):
        f = [None]*(n+1)
        f[0] = 0
        f[1] = 1
        for x in range(2, n+1):
            f[x] = f[x-1] + f[x-2]
        return f[n]
    

print(Solution().Fibonacci(9))
# 34
        
