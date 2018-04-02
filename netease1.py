# coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    length = int(sys.stdin.readline().strip())
    ans = 0
    # 读取矩阵点
    x1 = sys.stdin.readline().strip().split(' ')
    x1 = [int(x) for x in x1]
    y1 = sys.stdin.readline().strip().split(' ')
    y1 = [int(y) for y in y1]
    x2 = sys.stdin.readline().strip().split(' ')
    x2 = [int(x) for x in x2]
    y2 = sys.stdin.readline().strip().split(' ')
    y2 = [int(y) for y in y2]
    if length == 1:
        print 1
    same_num = [1 for i in range(length)]
    for i in range(length):
        for j in range(length):
            if i == j:
                continue
            # print i, j
            # print x1[i], y1[i], x2[i], y2[i], x1[j], y1[j], x2[j], y2[j]
            if (x1[j] < x2[i] or y1[j] < y2[i]) and (x2[j] > x1[i] or y2[j] > y1[i]):
                same_num[i] += 1
    # print same_num
    print max(same_num)