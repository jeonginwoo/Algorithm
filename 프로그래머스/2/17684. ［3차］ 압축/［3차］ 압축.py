def solution(msg):
    d = dict()
    for i in range(ord('Z')-ord('A')+1):
        d[chr(i+ord('A'))] = i+1
    
    answer = []
    now_idx = 27
    now_str = msg[0]
    for s in msg[1:]:
        temp = now_str + s
        if not d.get(temp):
            answer.append(d[now_str])
            d[temp] = now_idx
            now_idx += 1
            now_str = ""
        now_str += s
    answer.append(d[now_str])
    return answer