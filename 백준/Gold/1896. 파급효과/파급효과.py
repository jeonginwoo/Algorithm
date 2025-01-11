import sys
input = sys.stdin.readline

def IsLineValid(x, y):
    num = table[x][y]
    for i in range(1, num+1):
        if (x-i >= 0 and table[x-i][y] == num) or (y+i < C and table[x][y+i] == num) or (x+i < R and table[x+i][y] == num) or (y-i >= 0 and table[x][y-i] == num):
            return False
    return True
            
def dfs():
    for x in range(R):
        for y in range(C):
            if not IsLineValid(x, y):
                return False
            if visited[x][y]:
                continue
            stack = [(x, y)]
            visited[x][y] = True
            poli = {table[x][y]}
            while stack:
                nowX, nowY = stack.pop()
                for d in [(-1, 0, 1), (0, 1, 2), (1, 0, 4), (0, -1, 8)]:
                    if descr[nowX][nowY] & d[2]:
                        nextX = nowX + d[0]
                        nextY = nowY + d[1]
                        if not visited[nextX][nextY]:
                            if table[nextX][nextY] in poli:
                                return False
                            stack.append((nextX, nextY))
                            visited[nextX][nextY] = True
                            poli.add(table[nextX][nextY])
            for i in range(1, len(poli)+1):
                if i not in poli:
                    return False
    return True

T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    table = [list(map(int, input().strip())) for _ in range(R)]
    descr = [list(map(int, input().split())) for _ in range(R)]
    visited = [[False]*C for _ in range(R)]
    if dfs():
        print("valid")
    else:
        print("invalid")
