import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort()

result = float("inf")
l = r = 0
while l <= r and r < N:
    if A[r] - A[l] < M:
        r += 1
    else:
        result = min(result, A[r] - A[l])
        l += 1
print(result)