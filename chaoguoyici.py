# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        m = len(numbers) - 1
        for i in numbers:
            if i > m:
                ii = i - m - 1
            else:
                ii = i
            if numbers[ii] > m:
                duplication[0] = ii
                return True
            else:
                numbers[ii] += (m + 1)
        return False


res = [-1]
s = Solution()
print s.duplicate([2, 1, 3, 0, 4], res)
print res
