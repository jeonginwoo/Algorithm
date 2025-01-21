import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dist[0][0][K] = 1
    queue = deque([(0, 0, K)])
    
    while queue:
        nowX, nowY, k = queue.popleft()
        
        if nowX == N-1 and nowY == M-1:
            return dist[nowX][nowY][k]
        
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nextX, nextY = nowX+dx, nowY+dy
            
            if 0<=nextX<N and 0<=nextY<M:
                if matrix[nextX][nextY]=='0' and dist[nextX][nextY][k]==0:
                    dist[nextX][nextY][k] = dist[nowX][nowY][k] + 1
                    queue.append((nextX, nextY, k))
                    
                if matrix[nextX][nextY]=='1' and k>0 and dist[nextX][nextY][k-1]==0:
                    dist[nextX][nextY][k-1] = dist[nowX][nowY][k] + 1
                    queue.append((nextX, nextY, k-1))

    return -1

N, M, K = map(int, input().split())
matrix = [input().strip() for _ in range(N)]
dist = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

print(bfs())