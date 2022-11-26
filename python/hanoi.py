def print_hanoi(n, a=1, b=2, c=3):
    if n == 1:
        print(n, a, c)
        return 0
    else:
        print_hanoi(n-1, a, c, b)
        print(n, a, c)
        print_hanoi(n-1, b, a, c)
n = int(input())
print_hanoi(n)