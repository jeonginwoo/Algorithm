import sys
input = sys.stdin.readline

def check_max_length(board, N):
    max_length = 0
    for i in range(N):
        # 행에서 최대 길이 확인
        row_count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                row_count += 1
                max_length = max(max_length, row_count)
            else:
                row_count = 1

        # 열에서 최대 길이 확인
        col_count = 1
        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                col_count += 1
                max_length = max(max_length, col_count)
            else:
                col_count = 1

    return max_length

N = int(input())
board = [list(input().strip()) for _ in range(N)]
result = 0

for x in range(N):
    for y in range(N):
        # 오른쪽 교환
        if y + 1 < N:
            board[x][y], board[x][y+1] = board[x][y+1], board[x][y]
            result = max(result, check_max_length(board, N))
            board[x][y], board[x][y+1] = board[x][y+1], board[x][y]  # 복구

        # 아래쪽 교환
        if x + 1 < N:
            board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
            result = max(result, check_max_length(board, N))
            board[x][y], board[x+1][y] = board[x+1][y], board[x][y]  # 복구

print(result)
