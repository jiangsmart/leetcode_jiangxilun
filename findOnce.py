# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        d = {}
        for i in array:
            if d.get(i) == None:
                d[i] = 1
            else:
                d[i] += 1
        res = []
        for i in array:
            if d[i] == 1:
                res.append(i)
        return res
