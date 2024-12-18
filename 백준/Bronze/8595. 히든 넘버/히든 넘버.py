n = int(input())
s = input()

nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
sum = 0
val = '0'
for i in range(0, n):
    if s[i] in nums:
        val += s[i]
    elif val != '0':
        sum += int(val)
        val = '0'
sum += int(val)
print(sum)