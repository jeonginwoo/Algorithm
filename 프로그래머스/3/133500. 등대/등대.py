import sys
sys.setrecursionlimit(100000)

def solution(n, lighthouse):
    def dfs(now = 1):
        for next in edges[now]:
            if not visited[next]:
                visited[next] = True
                dfs(next)
                if not light[next]:
                    light[now] = True
    
    light = [False] * (n+1)
    visited = [False, True] + [False] * (n-1)
    edges = [[] for _ in range(n+1)]
    for a, b in lighthouse:
        edges[a].append(b)
        edges[b].append(a)
    
    dfs()
    
    return sum(light)