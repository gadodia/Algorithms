'''
This problem was recently asked by LinkedIn:

You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.
'''


def staircase(n):
    f = [None]*(n+1)
    f[0] = 1
    f[1] = 1
    for x in range(2, n+1):
        f[x] = f[x-1] + f[x-2]
    return f[n]
  
print(staircase(4))
# 5
print(staircase(5))
# 8