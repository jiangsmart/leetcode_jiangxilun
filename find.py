# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # print target,array[:][:-1]
        if len(array) == 0 or len(array[0]) == 0:
            return False
        if target == array[0][-1]:
            return True
        elif target < array[0][-1]:
            a = [r[:-1] for r in array]
            return self.Find(target, a)
        elif target > array[0][-1]:
            return self.Find(target, array[1:])


s = Solution()
print s.Find(7, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]])
