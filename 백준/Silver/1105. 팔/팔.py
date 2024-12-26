L, R = map(int, input().split())

count = 0
while L > 0 and R > 0:
    a = L % 10
    b = R % 10
    if a == b and a == 8:
        count += 1
    elif a != b:
        count = 0
    L //= 10
    R //= 10
        
if L != 0 or R != 0:
    count = 0
        
print(count)
