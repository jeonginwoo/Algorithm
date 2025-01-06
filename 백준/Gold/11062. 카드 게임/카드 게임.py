import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    dp = [[0]*N for _ in range(N)]
    
    turn = True if N % 2 == 1 else False
    for length in range(N):
        for left in range(N-length):
            right = left + length
            if length == 0:
                dp[left][right] = cards[left] if turn else 0
            elif turn:
                dp[left][right] = max(cards[left] + dp[left+1][right], cards[right] + dp[left][right-1])
            else:
                dp[left][right] = min(dp[left+1][right], dp[left][right-1])
        turn = not turn

    print(dp[0][N-1])