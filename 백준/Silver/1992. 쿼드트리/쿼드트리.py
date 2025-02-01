import sys
input = sys.stdin.readline

def func(x, y, n):
    now = video[x][y]
    
    check = True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if video[i][j] != now:
                check = False
                break
        if not check:
            break
    
    if check:
        return now
    else:
        half = n//2
        return "(" + func(x, y, half) + func(x, y+half, half) + func(x+half, y, half) + func(x+half, y+half, half) + ")"

N = int(input())
video = [input().strip() for _ in range(N)]
print(func(0, 0, N))