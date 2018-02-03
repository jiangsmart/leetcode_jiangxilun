# class Solution(object):
#     def __init__(self):
#         self.ans = list()
#         self.out = list()
#
#     def combinationSum(self, candidates, target):
#         length = len(candidates)
#         self.sumCore(candidates, target)
#         return self.out
#
#     def sumCore(self, candidates, target):
#         length = len(candidates)
#         for i in range(length):
#             if candidates[i] < target:
#                 self.ans.append(candidates[i])
#                 self.sumCore(candidates, target - candidates[i])
#             elif candidates[i] == target:
#                 self.ans.append(candidates[i])
#                 self.out.append(self.ans)
#                 self.ans.pop()
#                 return
#             elif i == length-1:
#                 self.ans.pop()
#                 return
#         return

# class Solution(object):
#     def combinationSum(self, candidates, target):
#         res = []
#         candidates.sort()
#         self.dfs(candidates, target, 0, [], res)
#         return res
#
#     def dfs(self, nums, target, index, path, res):
#         if target < 0:
#             return  # backtracking
#         if target == 0:
#             res.append(path)
#             return
#         for i in xrange(index, len(nums)):
#             self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

class Solution(object):
    def combinationSum(self, candidates, target):
        out = []
        candidates.sort()
        self.core(candidates, target, [], 0, out)
        return out

    def core(self, candidates, target, now, index, out):
        if target < 0:
            return
        if target == 0:
            out.append(now)
            return
        if target > 0:
            for i in xrange(index, len(candidates)):
                #now+=[candidates[i]]
                #now.append(candidates[i])
                print '1:now'
                print id(now)
                c=now+[candidates[i]]
                print 'c'
                print id(c)
                now=now+[candidates[i]]
                print '2:now'
                print id(now)
                #self.core(candidates, target - candidates[i], now + [candidates[i]], i, out)
                self.core(candidates, target - candidates[i], c[:], i, out)
            pass


s1 = Solution()
a = [2, 3, 6, 7]
b = 7
print s1.combinationSum(a, b)
# test1 = [1, 2, 3, 4]
# test2 = [1, 2, 3, 4]
# test1.append(5)
# test2=test2+[5]
# print test1
# print test2
