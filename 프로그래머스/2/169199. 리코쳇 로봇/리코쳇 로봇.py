from collections import deque

def solution(board):
    global n, m
    
    def print_board():
        for i in range(n):
            for j in range(m):
                print("1" if visited[i][j] else "0", end="")
            print()
        print()
    
    def next_dot(now, direction):
        x, y = now
        while 0 <= x < n and 0 <= y < m and board[x][y] != 'D':
            x += direction[0]
            y += direction[1]
        x -= direction[0]
        y -= direction[1]
        return (x, y)
        
    def bfs(start):
        visited = [[-1]*m for _ in range(n)]
        visited[start[0]][start[1]] = 0
        queue = deque([start])
        while queue:
            now = queue.popleft()
            nexts = []
            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nexts.append(next_dot(now, direction))
            for nextX, nextY in nexts:
                if visited[nextX][nextY] == -1:
                    visited[nextX][nextY] = visited[now[0]][now[1]] + 1
                    queue.append((nextX, nextY))
                    if board[nextX][nextY] == 'G':
                        return visited[nextX][nextY]
        return -1
    
    n = len(board)
    m = len(board[0])
    
    start = None
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
                break
        if start:
            break
    
    return bfs(start)