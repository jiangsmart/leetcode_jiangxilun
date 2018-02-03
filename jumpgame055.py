class Solution(object):
    def foo(self, nums):
        length = len(nums)
        reach=0
        for i in range(0, length):
            if i>reach:
                return False
            reach=max(i+nums[i],reach)
        return True

s1=Solution()
nums=[3,2,0,1,1]
print s1.foo(nums)