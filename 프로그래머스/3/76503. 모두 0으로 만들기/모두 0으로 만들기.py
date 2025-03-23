import sys
sys.setrecursionlimit(1000000)

def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    def dfs(now=0):
        nonlocal answer
        for next in tree[now]:
            if not visited[next]:
                visited[next] = True
                dfs(next)
                answer += abs(a[next])
                a[now] += a[next]
                a[next] = 0
    
    visited = [True]+[False for _ in range(len(a)-1)]
    tree = [[] for _ in range(len(a))]
    for x, y in edges:
        tree[x].append(y)
        tree[y].append(x)
    
    answer = 0
    dfs()
    
    return answer