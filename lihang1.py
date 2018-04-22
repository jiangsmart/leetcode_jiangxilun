#coding=utf8
import sys
def solve(changes,x):
    amount = x
    coins = changes
    dp = [0]*(amount+1)
    dp[0] = 1
    for coin in coins:
        for i in xrange(coin,amount+1):
            dp[i]+=dp[i-coin]
    return dp[amount]%100000007
#print(solve([1,2,5],5))
if __name__ == "__main__":
    # 读取第一行的n
    test_num = int(sys.stdin.readline())
    ans = []
    for i in xrange(test_num):
        #n,k = map(int,sys.stdin.readline().strip().split())
        #x = map(int,sys.stdin.readline().strip().split())
        n,k = [int(p) for p in sys.stdin.readline().strip().split()]
        x = [int(p) for p in sys.stdin.readline().strip().split()]
        r = solve(x,k)
        ans.append(r)
    for i in ans:
        print i