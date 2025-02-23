def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))
    now = 0
    answer = 0
    for target in targets:
        if now <= target[0]:
            now = target[1]
            answer += 1
    return answer