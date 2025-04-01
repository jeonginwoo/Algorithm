def solution(m, n, board):
    board = [list(x) for x in board]
    answer = 0
    while True:
        mark = [[False]*n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != " ":
                    mark[i][j] = mark[i+1][j] = mark[i][j+1] = mark[i+1][j+1] = True
        
        count = 0
        for i in range(m):
            count += sum(mark[i])
        if not count:
            break
        answer += count
        
        for i in range(m):
            for j in range(n):
                if mark[i][j]:
                    board[i][j] = " "
        
        for i in range(m-2, -1, -1):
            for j in range(n):
                k = i+1
                while k < m and board[k][j] == " ":
                    k += 1
                board[i][j], board[k-1][j] = board[k-1][j], board[i][j]
    
    return answer