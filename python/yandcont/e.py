tree = {}
n = int(input())

for i in range(3, n+1):
    ingr = list(map(int, input().split()))
    tree[i] = ingr[1:]


def check(num):
    queue = []
    count = 0
    c_l = [0 for _ in range(n)]
    queue.append(num)
    while queue:
        node = queue[0]
        queue = queue[1:]
        count += 1
        c_l[node-1] = 1
        if count > sum(c_l):
            return False
        if node in tree.keys():
            for i in tree[node]:
                if i != 1 and i != 2:
                    queue.append(i)
    return True

def count(num):
    if num == 1 or num == 2: return 0
    ans = 0
    for i in tree[num]:
        if i == 1: ans += 1
        if i == 2: ans += 1j
        ans += count(i)
    return ans


q = int(input())
Q = []
for _ in range(q):
    A, B, num = map(int, input().split())
    Q.append([A, B, num])
for query in Q:
    A, B, num = query
    if not check(num):
        print(0, end='')
    else:
        k = count(num)
        if k.real <= A and k.imag <= B:
            print(1, end='')
        else:
            print(0, end='')