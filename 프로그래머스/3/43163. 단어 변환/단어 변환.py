from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def check_neighbor(A:str, B:str):
        count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                if count == 1:
                    return False
                count += 1
        return True
    
    words.append(begin)
    
    n = len(words)
    edges = [[] for _ in range(n)]
    
    for i in range(n-1):
        for j in range(i+1, n):
            if check_neighbor(words[i], words[j]):
                edges[i].append(j)
                edges[j].append(i)
    
    start = -1
    end = words.index(target)
    visited = [-1]*n
    visited[start] = 0
    queue = deque([start])
    while queue:
        now = queue.popleft()
        for next in edges[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                if next == end:
                    return visited[next]
                queue.append(next)
    
    return 0