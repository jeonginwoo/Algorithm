N = int(input())

answer = []
div = 2
while div <= N:
    if N % div == 0:
        N /= div
        answer.append(div)
    else:
        div += 1
for i in answer:
    print(i)