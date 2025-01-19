import sys
input = sys.stdin.readline

def floyd_warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                T[i][j] = min(T[i][j], T[i][k] + T[k][j])

def dfs(now, visited_count, time):
    global result
    if visited_count == N:
        result = min(result, time)
        return
    if result <= time:
        return
    for next in range(N):
        if not visited[next]:
            visited[next] = True
            dfs(next, visited_count+1, time+T[now][next])
            visited[next] = False

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

floyd_warshall()
result = float("inf")
visited = [False] * N
visited[K] = True
dfs(K, 1, 0)

print(result)