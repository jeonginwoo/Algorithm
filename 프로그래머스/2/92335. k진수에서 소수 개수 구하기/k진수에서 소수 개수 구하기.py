def solution(n, k):
    def isPrime(num):
        if num <= 1:
            return False
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    
    new = ""
    while n > 0:
        new += str(n%k)
        n //= k
    nums = [int(x) for x in new[::-1].split("0") if x]
    
    answer = 0
    for num in nums:
        if isPrime(num):
            answer += 1
    
    return answer