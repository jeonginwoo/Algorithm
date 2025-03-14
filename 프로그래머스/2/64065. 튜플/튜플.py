def solution(s):
    a = [set(int(y) for y in x.split(',')) for x in s[2:len(s)-2].split("},{")]
    b = [None]*len(a)
    for x in a:
        b[len(x)-1] = x
    
    answer = [list(b[0])[0]]+[None]*(len(a)-1)
    for i in range(len(b)-1, 0, -1):
        answer[i] = list(b[i]-b[i-1])[0]
    return answer