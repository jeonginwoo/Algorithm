import sys
input = sys.stdin.readline

def isInCircle(x, y, cx, cy, r):
    return (x-cx)**2 + (y-cy)**2 < r**2

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        if isInCircle(x1, y1, cx, cy, r) or isInCircle(x2, y2, cx, cy, r):
            if not (isInCircle(x1, y1, cx, cy, r) and isInCircle(x2, y2, cx, cy, r)):
                count += 1
    print(count)
