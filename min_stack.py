# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        return

    def push(self, node):
        self.stack.append(node)
        if self.min_stack == [] or node < self.min_stack[-1]:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min_stack[-1])
        return

    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def min(self):
        if self.stack:
            return self.min_stack[-1]

s=Solution()
s.push(1)
print s.min()
s.push(2)
print s.min()
s.push(0)
print s.min()