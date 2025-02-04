def solution(diffs, times, limit):
    def solve_time(diff, time_cur, time_prev, level):
        if diff <= level:
            return time_cur
        else:
            return (time_cur + time_prev) * (diff - level) + time_cur
    
    times.append(1)
    MAX_DIFF = 100000
    
    answer = 0
    left = 1
    right = MAX_DIFF
    while left <= right:
        mid = (left+right) // 2
        clear_time = sum([solve_time(diffs[i], times[i], times[i-1], mid) for i in range(len(diffs))])
        if clear_time > limit:
            left = mid+1
        else:
            right = mid-1
    return right+1