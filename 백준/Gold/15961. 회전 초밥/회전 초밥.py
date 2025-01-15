import sys
input = sys.stdin.readline  

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]

count = 1
select = [0]*(d+1)
select[c] = 1
for i in range(k):
    select[belt[i]] += 1
    if select[belt[i]] == 1:
        count += 1

result = count
for i in range(N):
    select[belt[i]] -= 1
    if select[belt[i]] == 0:
        count -= 1
    
    select[belt[(i+k)%N]] += 1
    if select[belt[(i+k)%N]] == 1:
        count += 1
    
    result = max(result, count)

print(result)