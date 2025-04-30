from collections import defaultdict

def solution(gems):
    n = len(set(gems))
    if n == 1:
        return [1, 1]
    
    answer = []
    min_len = float("inf")
    left = right = 0
    count = defaultdict(int)
    count[gems[0]] += 1
    while right < len(gems)-1:
        if len(count) < n:
            right += 1
            count[gems[right]] += 1
        else:
            if right - left < min_len:
                min_len = right - left
                answer = [left+1, right+1]
            count[gems[left]] -= 1
            if count[gems[left]] == 0:
                del count[gems[left]]
            left += 1
    while left < len(gems):
        if len(count) == n and right - left < min_len:
            min_len = right - left
            answer = [left+1, right+1]
        count[gems[left]] -= 1
        if count[gems[left]] == 0:
            del count[gems[left]]
        left += 1
        
    return answer