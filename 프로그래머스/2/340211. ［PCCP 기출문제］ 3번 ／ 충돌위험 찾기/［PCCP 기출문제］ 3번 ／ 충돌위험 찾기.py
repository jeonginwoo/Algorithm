def solution(points, routes):
    now = points[:]
    # visited[time][r][c]
    visited = [[[0]*101 for _ in range(101)] for _ in range(20000)]
    
    answer = 0
    for route in routes:
        time = 0
        for i in range(1, len(route)):
            start_r, start_c = points[route[i-1]-1]
            end_r, end_c = points[route[i]-1]
            for r in range(start_r, end_r, -1 if start_r > end_r else 1):
                if visited[time][r][start_c] == 1:
                    answer += 1
                visited[time][r][start_c] += 1
                time += 1
            for c in range(start_c, end_c, -1 if start_c > end_c else 1):
                if visited[time][end_r][c] == 1:
                    answer += 1
                visited[time][end_r][c] += 1
                time += 1
        end_r, end_c = points[route[-1]-1]
        if visited[time][end_r][end_c] == 1:
            answer += 1
        visited[time][end_r][end_c] += 1
    
    return answer