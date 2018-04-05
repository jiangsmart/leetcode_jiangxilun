# # coding=utf-8
# # 链接：https://www.nowcoder.com/questionTerminal/46e837a4ea9144f5ad2021658cb54c4d
# # 来源：牛客网
#
# import sys
# import bisect
#
# task = {}
# lines = sys.stdin.readlines()
# n, m = map(int, lines[0].strip().split())  # 由于有空行，这句可以不写
# for line in lines[1:-1]:
#     if not line.strip().split():  # 存在空行，你能信...
#         continue
#     a, b = map(int, line.strip().split()) # a难度，b报酬
#     task[a] = max(task.get(a, 0), b)      # 建hash表，key为难度，value为该难度下最高的回报
# arr = sorted(task.keys())
# for i in range(1, len(arr)):              # 规整hash表，key大的value也大
#     if task[arr[i]] < task[arr[i - 1]]:
#         task[arr[i]] = task[arr[i - 1]]
# skills = map(int, lines[-1].strip().split())
# for skill in skills:
#     if skill in task:
#         print(task[skill])
#     else:
#         ind = bisect.bisect(arr, skill)
#         if ind == 0:
#             print(0)
#         else:
#             print(task[arr[ind - 1]])

# coding=utf-8
n, m = map(int, raw_input().strip().split())
jobs = {}
for i in range(n):
    diff, reward = map(int, raw_input().strip().split())
    jobs[diff] = max(jobs.get(diff, 0), reward)
stus = map(int, raw_input().strip().split())
sort_diff = sorted(jobs.keys())  # 返回list，取值用values()
print
for i in range(1, len(sort_diff)):
    if jobs[sort_diff[i]] < jobs[sort_diff[i - 1]]:
        jobs[sort_diff[i]] = jobs[sort_diff[i - 1]]
print jobs
for stu in stus:
    i = 0
    while i < len(sort_diff) and stu >= sort_diff[i]:
        i += 1
    print jobs[sort_diff[i - 1]]
