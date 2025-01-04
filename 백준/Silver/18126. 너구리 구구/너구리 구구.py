import sys
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)]
for i in range(N-1):
    A, B, C = map(int, input().split())
    edges[A].append((B, C))
    edges[B].append((A, C))

stack = [1]
visited = [False] * (N+1)
visited[1] = True
dist = [0]*(N+1)
while stack:
    nowRoom = stack.pop()
    for nextRoom, nextCost in edges[nowRoom]:
        if not visited[nextRoom]:
            stack.append(nextRoom)
            visited[nextRoom] = True
            dist[nextRoom] = dist[nowRoom] + nextCost
print(max(dist))