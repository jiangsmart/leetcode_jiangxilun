import sys


def cal(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        dp = [[1, 0], [1, 1]]
        for i in range(2, n):
            d1 = dp[-1][0] + dp[-1][1]
            d2 = dp[-2][0]
            dp.append([d1, d2])
        return dp[-1][0] + dp[-1][1]


if __name__ == '__main__':
    data = sys.stdin.readline()
    num = int(data)
    res = cal(num)
    print res
