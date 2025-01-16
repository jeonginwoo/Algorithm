import sys
input = sys.stdin.readline

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort(key=lambda x: (x[0], -x[1]))

left, right = lines[0][0], lines[0][1]
dist = right - left
for i in range(1, N):
    if lines[i][0] == lines[i-1][0] or lines[i][1] <= right:
        continue
    if lines[i][1] > right and lines[i][0] <= right:
        dist += lines[i][1] - right
    else:
        dist += lines[i][1] - lines[i][0]
        left = lines[i][0]
    right = lines[i][1]

print(dist)