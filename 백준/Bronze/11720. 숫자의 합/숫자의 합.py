N = int(input())
num = input()
answer = 0

for i in range(N-1, -1, -1):
    answer += int(num[i])
print(answer)