import sys
import math


def solve_n(n):
    res = [0,0,1]
    for i in range(3,n+1):
        res.append((i-1)*(res[i-1]+res[i-2]))
    return res[-1]

def solve_nn(n):
    if n%2==0:
        return n*solve_n(n-1)
    else:
        return n*solve_n(n-1)

if __name__ == '__main__':
    data = sys.stdin.readline()
    num = int(data)
    res = solve_nn(num)
    print res



