# coding=utf8
def solve(nh, x):
    n = nh
    nums = x
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0], dp[1] = 0, nums[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    answer = dp[n - 1]
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return max(dp[n - 2], answer)


import sys

if __name__ == "__main__":
    # 读取第一行的n
    test_num = int(sys.stdin.readline())
    ans = []
    for i in range(test_num):
        nh = int(sys.stdin.readline())
        x = map(int, sys.stdin.readline().strip().split())
        r = solve(nh, x)
        ans.append(r)
    for i in ans:
        print i