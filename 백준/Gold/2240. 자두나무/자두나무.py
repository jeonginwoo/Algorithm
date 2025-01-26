import sys
input = sys.stdin.readline

T, W = map(int, input().split())
tree = [int(input()) for _ in range(T)]

dp = [[0]*(W+1) for _ in range(T+1)]
for t in range(1, T+1):
    for w in range(W+1):
        now = tree[t-1]
        dp[t][w] = dp[t-1][w] + (1 if 1+w%2 == now else 0)
        if w > 0:
            dp[t][w] = max(dp[t][w], dp[t-1][w-1] + (1 if 1+w%2 == now else 0))

print(max(dp[T]))