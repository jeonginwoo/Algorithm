import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            T[i][j] = min(T[i][j], T[i][k]+T[k][j])

for _ in range(M):
    start, end, time = map(int, input().split())
    print("Enjoy other party" if T[start-1][end-1] <= time else "Stay here")