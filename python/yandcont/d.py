s1 = []
s2 = []
n = int(input())

for _ in range(n):
    start, end, cost = map(int, input().split())
    s1.append([start, cost])
    s2.append([end, end-start])

s1 = sorted(s1, key=lambda x:x[0])
for i in range(1, n):
    s1[i][1] += s1[i-1][1]

s2 = sorted(s2, key= lambda x:x[0])
for i in range(1, n):
    s2[i][1] += s2[i-1][1]

Q = []
q = int(input())
for _ in range(q):
    start, end, type_ = map(int, input().split())
    Q.append([start, end, type_])

for query in Q:
    start, end, type_ = query
    if type_ == 1:
        ans1 = [i for i in s1 if i[0] <= end]
        dans = [i for i in s1 if start > i[0]]
        ans = ans1[-1][1] if ans1 else 0
        print(ans - dans[-1][1] if dans else ans)
    elif type_ == 2:
        ans2 = [i for i in s2 if i[0] <= end]
        ans = ans2[-1][1] if ans2 else 0
        dans = [i for i in s2 if start > i[0]]
        print(ans-dans[-1][1] if dans else ans)