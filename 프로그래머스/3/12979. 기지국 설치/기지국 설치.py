import math

def solution(n, stations, w):
    answer = 0
    left = 1
    for station in stations:
        right = station - w
        if right > left:
            answer += math.ceil((right - left) / (2*w+1))
        left = station + w + 1
    right = n+1
    if right > left:
        answer += math.ceil((right - left) / (2*w+1))
    return answer
