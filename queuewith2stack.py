# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        return

    def push(self, node):
        self.stack1.append(node)
        return

    def pop(self):
        # return xx
        res = 0
        if self.stack1:
            while len(self.stack1) > 1:
                self.stack2.append(self.stack1.pop())
            res = self.stack1.pop()
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            return res