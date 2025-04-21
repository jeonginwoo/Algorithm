def solution(routes):
    routes.sort(key=lambda x: (x[1], x[0]))
    print(routes)
    now = routes[0][1]
    answer = 1
    for route in routes:
        if route[0] <= now:
            continue
        now = route[1]
        answer += 1
    return answer