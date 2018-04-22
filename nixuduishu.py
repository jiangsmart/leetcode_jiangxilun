# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        num = self.merge_sort(data, 0)
        return num[1]%1000000007

    def merge_sort(self, arr, num):
        # write code here
        length = len(arr)
        if length > 1:
            mid = length / 2
            left, a = self.merge_sort(arr[:mid], num)
            right, b = self.merge_sort(arr[mid:], num)
            l, n = self.merge(left, right, num)
            #print n
            num += a
            num += b
            num += n
            return l, num
        else:
            return arr, num

    def merge(self, arr1, arr2, num):
        res = []
        length1 = len(arr1)
        length2 = len(arr2)
        i1, i2 = 0, 0
        while i1 < length1 and i2 < length2:
            if arr1[i1] <= arr2[i2]:
                res.append(arr1[i1])
                i1 += 1
            else:
                num += len(arr1)-i1
                res.append(arr2[i2])
                i2 += 1
        res += arr1[i1:]
        res += arr2[i2:]
        return res, num


s = Solution()
a = s.InversePairs([1,2,3,4,5,6,7,0])
print a
