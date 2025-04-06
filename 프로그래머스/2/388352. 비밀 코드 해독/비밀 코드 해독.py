from itertools import combinations

def solution(n, q, ans):
    candidates = combinations(range(1, n + 1), 5)
    count = 0
    
    for candidate in candidates:
        valid = True
        candidate_set = set(candidate)
        for query, expected in zip(q, ans):
            match = len(candidate_set & set(query))
            if match != expected:
                valid = False
                break
        if valid:
            count += 1
    return count
