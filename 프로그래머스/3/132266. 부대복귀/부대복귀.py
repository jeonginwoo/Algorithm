from collections import deque

def solution(n, roads, sources, destination):
    edges = [[] for _ in range(n+1)]
    for a, b in roads:
        edges[a].append(b)
        edges[b].append(a)
    
    answer = []
    dist = [-1]*(n+1)
    dist[destination] = 0
    visited = [False] * (n+1)
    visited[destination] = True
    queue = deque([destination])
    while queue:
        now = queue.popleft()
        check = False
        for next in edges[now]:
            if visited[next]:
                continue
            dist[next] = dist[now] + 1
            if next == destination:
                check = True
                break
            visited[next] = True
            queue.append(next)
        if check:
            break
    answer = [dist[start] for start in sources]
        
    return answer