import sys
input = sys.stdin.readline

N = int(input())
T, P = zip(*[map(int, input().split()) for _ in range(N)])

dp = [0]*(N+1)
for i in range(N-1, -1, -1):
    if i+T[i] <= N:
        dp[i] = max(dp[i+1], dp[i+T[i]]+P[i])
    else:
        dp[i] = dp[i+1]
print(dp[0])