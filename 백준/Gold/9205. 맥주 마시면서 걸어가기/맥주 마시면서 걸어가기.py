import sys
input = sys.stdin.readline

def dot_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def dfs():
    stack = [nodes[0]]
    visited[0] = True
    while stack:
        now = stack.pop()
        for next in nodes:
            if not visited[next[-1]] and dot_dist(now, next) <= 1000:
                if next == nodes[-1]:
                    return True
                visited[next[-1]] = True
                stack.append(next)
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    nodes = [list(map(int, input().split()))+[i] for i in range(n+2)]
    visited = [False]*(n+2)
    print("happy" if dfs() else "sad")