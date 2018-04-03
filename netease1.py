# coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    # length = int(sys.stdin.readline().strip())
    # ans = 0
    # # 读取矩阵点
    # x1 = sys.stdin.readline().strip().split(' ')
    # x1 = [int(x) for x in x1]
    # y1 = sys.stdin.readline().strip().split(' ')
    # y1 = [int(y) for y in y1]
    # x2 = sys.stdin.readline().strip().split(' ')
    # x2 = [int(x) for x in x2]
    # y2 = sys.stdin.readline().strip().split(' ')
    # y2 = [int(y) for y in y2]
    # if length == 1:
    #     print 1
    # same_num = [1 for i in range(length)]
    # for i in range(length):
    #     for j in range(length):
    #         if i == j:
    #             continue
    #         # print i, j
    #         # print x1[i], y1[i], x2[i], y2[i], x1[j], y1[j], x2[j], y2[j]
    #         if (x1[j] < x2[i] or y1[j] < y2[i]) and (x2[j] > x1[i] or y2[j] > y1[i]):
    #             same_num[i] += 1
    # # print same_num
    # print max(same_num)


    lines = sys.stdin.readlines()
    n = int(lines[0])
    x1 = list(map(int, lines[1].split()))
    y1 = list(map(int, lines[2].split()))
    x2 = list(map(int, lines[3].split()))
    y2 = list(map(int, lines[4].split()))
    # 遍历所有点的组合（包含了矩形所有角以及交点），看一下有多少矩形包含它
    res = 1
    for x in x1 + x2:
        for y in y1 + y2:
            cnt = 0
            for i in range(n):
                if x > x1[i] and y > y1[i] and x <= x2[i] and y <= y2[i]:
                    cnt += 1
            res = max(res, cnt)
    print(res)
