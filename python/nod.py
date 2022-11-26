a, b = map(int, input().split())
if a < b:
    a,b = b,a
while b > 0:
    a,b = b, a%b
print(a)
continue