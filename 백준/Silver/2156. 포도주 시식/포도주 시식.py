import sys
input = sys.stdin.readline

n = int(input())
podo = [0]+list(map(int, sys.stdin.read().splitlines()))

if n == 1:
    print(podo[1])
    exit()
if n == 2:
    print(podo[1] + podo[2])
    exit()

dp = [0]*(n+1)
dp[1] = podo[1]
dp[2] = podo[1] + podo[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-2], max(dp[:i-2]) + podo[i-1]) + podo[i]
print(max(dp))