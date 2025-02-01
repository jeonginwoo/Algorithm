import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())
a_sqrt = math.ceil(a**(0.5))
b_sqrt = int(b**(0.5))
count = set()
for num in range(2, b_sqrt+1):
    if num == 1:
        continue
    square = num*num
    now = max(square, ((a+square-1)//square) * square)
    i = 2
    while now <= b:
        count.add(now)
        now += square
print(b-a+1 - len(count))