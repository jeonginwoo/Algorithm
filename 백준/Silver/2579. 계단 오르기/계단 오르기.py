import sys
input = sys.stdin.readline

N = int(input())
points = list(map(int, sys.stdin.read().splitlines()))

if N == 1:
    print(points[0])
    exit()
if N == 2:
    print(points[0] + points[1])
    exit()

dp = [0]*N
dp[0] = points[0]
dp[1] = points[0]+points[1]
for i in range(2, N):
    dp[i] = max(dp[i-2], dp[i-3]+points[i-1]) + points[i]
print(dp[-1])