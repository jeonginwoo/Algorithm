lenA, lenB = [int(x) for x in input().split()]
A = set([int(x) for x in input().split()])
B = set([int(x) for x in input().split()])

result = len(A) + len(B)
for a in A:
    if a in B:
        result -= 2
print(result)