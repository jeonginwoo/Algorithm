def solution(n, t, m, p):
    def decimal_to_base(num, base):
        if num == 0:
            return "0"
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while num:
            result = digits[num % base] + result
            num //= base
        return result
    
    result = ''
    for i in range(t*m):
        result += decimal_to_base(i, n)
    
    answer = ''
    for i in range(p-1, p-1+m*t, m):
        answer += result[i]
    return answer