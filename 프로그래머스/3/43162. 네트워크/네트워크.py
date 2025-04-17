def solution(n, computers):
    edges = [[] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                edges[i].append(j)
                edges[j].append(i)
    
    answer = 0
    visited = [False]*n
    for start in range(n):
        if visited[start]:
            continue
        stack = [start]
        visited[start] = True
        while stack:
            now = stack.pop()
            for next in edges[now]:
                if not visited[next]:
                    stack.append(next)
                    visited[next] = True
        answer += 1
    
    return answer