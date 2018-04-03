# coding=utf-8
# 链接：https://www.nowcoder.com/questionTerminal/46e837a4ea9144f5ad2021658cb54c4d
# 来源：牛客网

import sys
import bisect

task = {}
lines = sys.stdin.readlines()
n, m = map(int, lines[0].strip().split())  # 由于有空行，这句可以不写
for line in lines[1:-1]:
    if not line.strip().split():  # 存在空行，你能信...
        continue
    a, b = map(int, line.strip().split())
    task[a] = max(task.get(a, 0), b)
arr = sorted(task.keys())
for i in range(1, len(arr)):
    if task[arr[i]] < task[arr[i - 1]]:
        task[arr[i]] = task[arr[i - 1]]
skills = map(int, lines[-1].strip().split())
for skill in skills:
    if skill in task:
        print(task[skill])
    else:
        ind = bisect.bisect(arr, skill)
        if ind == 0:
            print(0)
        else:
            print(task[arr[ind - 1]])
