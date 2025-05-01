from collections import deque

def solution(n, edge):
    edges = [[] for _ in range(n+1)]
    for a, b in edge:
        edges[a].append(b)
        edges[b].append(a)
    
    queue = deque([1])
    visited = [-1] * (n+1)
    visited[1] = 0
    max_dist = 0
    while queue:
        now = queue.popleft()
        for next in edges[now]:
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[now] + 1
                max_dist = max(max_dist, visited[next])
    
    answer = 0
    for i in range(1, n+1):
        if visited[i] == max_dist:
            answer += 1
    return answer