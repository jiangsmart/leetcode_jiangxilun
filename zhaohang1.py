# coding=utf-8
import sys
import math

test_num = int(sys.stdin.readline())
type_nums = []
sums = []
for i in range(test_num):
    type_num, sum = map(int, sys.stdin.readline().strip().split())
    types = map(int, sys.stdin.readline().strip().split())
    dp = []
    types.sort()
    for i in range(type_num + 1):
        dpp = []
        for j in range(sum + 1):
            dpp.append(0)
        dp.append(dpp)
    for i in range(1, type_num + 1):
        for j in range(sum + 1):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = 0
                for xi in range(int(math.floor(j / types[i])) + 1):
                    dp[i][j] += dp[i - 1][j - (xi * types[i])]
    print dp

    # # print type_num, sum, types
    # dp = [0 for i in range(sum+1)]
    # if sum == 0 or type_num == 0:
    #     print 0
    #     break
    # types.sort()
    # for i in range(1, sum + 1):
    #     for j in range(0, type_num):
    #         if types[j] > i: break;
    #         dp[i] = max(dp[i], dp[i - types[j]] + 1) % 100000007
    # print dp
    # print dp[sum]
