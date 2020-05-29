'''
 This problem was recently asked by Twitter:

Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max() which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.
'''

class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxstack = []

    def push(self, val):
        self.stack.append(val)
        if not self.maxstack or val >= self.maxstack[-1]:
            self.maxstack.append(val)            

    def pop(self):
        if not self.stack:
            return None
        val = self.stack.pop()
        if self.maxstack and self.maxstack[-1] == val:
            self.maxstack.pop()        

    def max(self):
        if self.maxstack:
            return self.maxstack[-1]
        return None


s = MaxStack()
s.push(1)
s.push(3)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 3
s.pop()
# 3
print(s.max())
s.pop()
# 1
print(s.max())