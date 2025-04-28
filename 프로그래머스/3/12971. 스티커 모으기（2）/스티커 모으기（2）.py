def solution(sticker):
    n = len(sticker)
    if n <= 2:
        return max(sticker)
    
    dp1 = [sticker[0], sticker[1], sticker[0] + sticker[2]] + [0]*(n-3)
    dp2 = [0, sticker[1], sticker[2]] + [0]*(n-3)
    
    for i in range(3, n):
        dp1[i] = max(dp1[i-2]+sticker[i], dp1[i-3]+sticker[i])
        dp2[i] = max(dp2[i-2]+sticker[i], dp2[i-3]+sticker[i])
    dp1[-1] = 0
    return max(max(dp1), max(dp2))