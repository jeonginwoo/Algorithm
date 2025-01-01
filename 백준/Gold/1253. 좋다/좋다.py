import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
num_count = defaultdict(int)
for num in A:
    num_count[num] += 1

result = 0
for i in range(N):
    for j in range(N):
        diff = A[i] - A[j]
        num_count[A[i]] -= 1
        num_count[A[j]] -= 1
        num_count[diff] -= 1
        check = False
        if i != j and num_count[diff] >= 0:
            result += 1
            check = True
        num_count[A[i]] += 1
        num_count[A[j]] += 1
        num_count[diff] += 1
        if check:
            break
print(result)