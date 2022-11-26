a = [0]*31
a[1] = 1
for i in range(2, 31):
    a[i] = a[i-1] + a[i-2]
n = int(input())
print(a[n])