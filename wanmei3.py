# coding=utf-8
import sys

if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()
    line3 = sys.stdin.readline().strip()
    n = int(line1)
    arrive = list(map(int, line2.split()))
    leave = list(map(int, line3.split()))
    res = 1
    for time in arrive + leave:
        cnt = 0
        for i in range(n):
            if time >= arrive[i] and time < leave[i]:
                cnt += 1
        res = max(res, cnt)
    print res
