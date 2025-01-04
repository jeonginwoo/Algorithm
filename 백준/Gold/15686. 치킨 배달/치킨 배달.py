import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            houses.append((r, c))
        elif board[r][c] == 2:
            chickens.append((r, c))

dist = []
for hx, hy in houses:
    dist_row = []
    for cx, cy in chickens:
        dist_row.append(abs(hx - cx) + abs(hy - cy))
    dist.append(dist_row)

min_dist_sum = float('inf')
for combo in combinations(range(len(chickens)), M):
    tmp_sum = 0
    for h in range(len(houses)):
        tmp_sum += min(dist[h][c] for c in combo)
        if tmp_sum > min_dist_sum:
            break
    
    min_dist_sum = min(min_dist_sum, tmp_sum)

print(min_dist_sum)
