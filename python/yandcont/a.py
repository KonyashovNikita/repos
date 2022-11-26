n = int(input())
for _ in range(n):
    info = input().split(',')
    sum1 = len(set(info[0] + info[1] + info[2]))
    sum2 = (int(info[3])//10 + int(info[3])%10 + int(info[4])//10 + int(info[4])%10) * 64
    sum3 = (ord(info[0].lower()[0]) - 96) * 256
    summa = (sum1 + sum2 +sum3) % 4096
    print(hex(summa+4096).upper()[-3:])