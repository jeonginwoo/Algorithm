import sys
input = sys.stdin.readline

def dfs(now, dist):
    if now == b:
        return dist
    result = 0
    for next, d in edges[now]:
        if not visited[next]:
            visited[next] = True
            result += dfs(next, dist+d)
    return result
        

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

for _ in range(M):
    a, b = map(int, input().split())
    visited = [False]*(N+1)
    visited[a] = True
    print(dfs(a, 0))