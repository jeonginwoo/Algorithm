def solution(sequence, k):
    n = len(sequence)
    left = right = 0
    part_sum = sequence[0]
    answer = [0, float('inf')]
    while left <= right < n:
        if part_sum == k and right-left < answer[1]-answer[0]:
            answer = [left, right]
        if part_sum <= k and right != n-1:
            right += 1
            part_sum += sequence[right]
        else:
            part_sum -= sequence[left]
            left += 1
    
    return answer