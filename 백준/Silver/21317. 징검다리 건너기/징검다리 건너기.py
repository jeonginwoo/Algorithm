import sys
input = sys.stdin.readline

N = int(input())
jump = [list(map(int, input().split())) for _ in range(N-1)]
k = int(input())


result = []
for i in range(N):
    dp = [float('inf')] * N
    dp[0] = 0
    for j in range(1, N):
        if j == 1:
            dp[j] = jump[0][0]
        elif j >= 3 and i == j:
            dp[j] = dp[j-3] + k
        else:
            dp[j] = min(dp[j-1] + jump[j-1][0], dp[j-2] + jump[j-2][1])
    result.append(dp[-1])

print(min(result))