import sys

input = sys.stdin.readline


def DFS():
    global N, danzi
    start = []
    visited = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if danzi[x][y] == "1":
                start.append((x, y))

    result = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for x, y in start:
        if not visited[x][y]:
            count = 0
            stack = []
            stack.append((x, y))
            visited[x][y] = True
            while stack:
                now_x, now_y = stack.pop()
                count += 1
                for go in range(4):
                    next_x = now_x + dx[go]
                    next_y = now_y + dy[go]
                    if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y] and danzi[next_x][next_y] == "1":
                        stack.append((next_x, next_y))
                        visited[next_x][next_y] = True
            result.append(count)
            result.sort()
    return result


N = int(input())
danzi = [input().strip() for _ in range(N)]
result = DFS()
print(len(result))
print(*result, sep="\n")
