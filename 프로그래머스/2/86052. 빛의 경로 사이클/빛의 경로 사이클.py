def solution(grid):
    def getDirection(prevDirection, route):
        if  route == 'S':
            return prevDirection
        elif route == 'L':
            return (prevDirection+3)%4
        else:
            return (prevDirection+1)%4
    
    def getNext(now):
        nowX, nowY, nowDirection = now
        nextX = (nowX + d[nowDirection][0] + N) % N
        nextY = (nowY + d[nowDirection][1] + M) % M
        nextDirection = getDirection(nowDirection, grid[nextX][nextY])
        return (nextX, nextY, nextDirection)
    
    N = len(grid)
    M = len(grid[0])
    visited = [[[False]*4 for _ in range(M)] for _ in range(N)]
    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    answer = []
    for i in range(N):
        for j in range(M):
            for k in range(4):
                if visited[i][j][k]:
                    continue
                stack = [(i, j, k)]
                visited[i][j][k] = True
                distance = 1
                while stack:
                    now = stack.pop()
                    next = getNext(now)
                    if not visited[next[0]][next[1]][next[2]]:
                        visited[next[0]][next[1]][next[2]] = True
                        stack.append(next)
                        distance += 1
                answer.append(distance)
    answer.sort()
    return answer