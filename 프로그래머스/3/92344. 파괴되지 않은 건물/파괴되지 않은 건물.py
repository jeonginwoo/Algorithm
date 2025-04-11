def solution(board, skill):
    n, m = len(board), len(board[0])
    diff = [[0]*(m+1) for _ in range(n+1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        count = -degree if type == 1 else degree
        diff[r1][c1] += count
        diff[r1][c2+1] -= count
        diff[r2+1][c1] -= count
        diff[r2+1][c2+1] += count
    
    for i in range(n):
        for j in range(1, m):
            diff[i][j] += diff[i][j-1]
    
    for j in range(m):
        for i in range(1, n):
            diff[i][j] += diff[i-1][j]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += diff[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer