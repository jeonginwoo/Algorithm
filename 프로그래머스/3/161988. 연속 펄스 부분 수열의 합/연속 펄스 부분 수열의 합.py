def solution(sequence):
    N = len(sequence)
    for i in range(0, N, 2):
        sequence[i] = -sequence[i]
    answer = 0
    ptr = 0
    sum1 = 0
    sum2 = 0
    while ptr < N:
        sum1 += sequence[ptr]
        sum2 += -sequence[ptr]
        answer = max(answer, sum1, sum2)
        
        sum1 = max(sum1, 0)
        sum2 = max(sum2, 0)
        ptr += 1
        
    return answer