from collections import Counter
a = "1231234"
b = Counter(a)
print([b[i] for i in b.keys()])