n = int(input())
flag = True
while n > 1:
    digit_s = 0
    while n > 0:
        digit_s += (n%10) ** 2
        n //= 10
    n = digit_s
    if n == 4:
        flag = False
        break
print(flag)