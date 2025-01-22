import sys
input = sys.stdin.readline

def count_joka(length:int):
    count = 0
    for l in L:
        count += l // length
    return count
    
M, N = map(int, input().split())
L = list(map(int, input().split()))
L.sort()

result = 0
left = 1
right = L[-1]
while left <= right:
    mid = (left + right) // 2
    if count_joka(mid) >= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)