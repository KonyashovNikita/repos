from collections import Counter
n = int(input())

def is_diverse(string):
    count = Counter(string)
    ln = len(count)
    num = [count[i] for i in count.keys()]
    maxim = max(num)
    return maxim <= ln

for _ in range(n):
    l = int(input())
    s = input()
    k = 0 
    for i in range(l):
        for j in range(i+1, l+1):
            if is_diverse(s[i:j]):
                k += 1
    print(k)