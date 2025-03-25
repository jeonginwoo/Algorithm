def solution(n, t, m, p):
    def decimal_to_base(num, base):
        if num == 0:
            return "0"
        digits = "0123456789ABCDEF"
        result = ""
        while num:
            result = digits[num % base] + result
            num //= base
        return result
    
    result = ''
    max_len = p-1+m*t
    i = 0
    while len(result) < max_len:
        result += decimal_to_base(i, n)
        i+=1
    
    return result[p-1:max_len:m]