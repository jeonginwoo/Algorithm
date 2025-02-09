def solution(edges):
    def dfs():
        visited[start] = True
        stack = [start]
        while stack:
            now = stack.pop()
            if len(rode[now]) == 0:
                answer[2] += 1
                return
            if len(rode[now]) == 2:
                answer[3] += 1
                return
            for next in rode[now]:
                if visited[next]:
                    answer[1] += 1
                    return
                else:
                    stack.append(next)
                    visited[next] = True
        
    
    A, B = zip(*edges)
    MAX_NODE = max(max(A), max(B))
    answer = [0, 0, 0, 0]
    
    rode = [[] for _ in range(MAX_NODE+1)]
    for a, b in edges:
        rode[a].append(b)
    
    count = [0]*(MAX_NODE+1)
    for a, b in edges:
        count[b] += 1
    for i in range(1, len(count)):
        if count[i] == 0 and len(rode[i]) >= 2:
            answer[0] = i
            break
    
    visited = [False]*(MAX_NODE+1)
    for start in rode[answer[0]]:
        dfs()
    
    return answer