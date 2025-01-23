import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
alphabets = sorted(input().split())
A = []
B = []
for a in alphabets:
    if a in ['a', 'e', 'i', 'o', 'u']:
        A.append(a)
    else:
        B.append(a)

result = []
for i in range(1, L-1):
    if i > 5 or L-i < 2:
        break
    A_combi = list(combinations(A, i))
    B_combi = list(combinations(B, L-i))
    for a in A_combi:
        for b in B_combi:
            temp = ['' for _ in range(ord('a'), ord('z')+1)]
            for c in a:
                temp[ord(c)-ord('a')] = c
            for d in b:
                temp[ord(d)-ord('a')] = d
            result.append(''.join(temp))
result.sort()
print(*result, sep='\n')