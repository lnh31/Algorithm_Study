import sys
input = sys.stdin.readline

n = int(input())
cases = [int(input()) for _ in range(n)]
dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3

for i in range(7, 101):
    dp[i] = dp[i-1] + dp[i-5]

for j in cases:
    print(dp[j])
