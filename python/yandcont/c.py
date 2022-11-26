n, q = map(int, input().split())
tree = {i:[i*2, i*2+1 if i*2+1 <= n else -1] for i in range(1, n//2 + 1)}
tree_r = {i:i//2 for i in range(2, n+1)}
root = 1
changes = list(map(int, input().split()))

for v in changes:
    if v in tree_r.keys():
        if v in tree.keys():
            p = tree_r[v]
            if p in tree_r.keys():
                pp = tree_r[p]
                dp = tree[p][(tree[p].index(v)+1) % 2]
                nv = tree[v][tree[p].index(v)]
                dv = tree[v][(tree[p].index(v)+1) % 2]
                p_ind = tree[pp].index(p)
                v_ind = tree[p].index(v)
                tree_r[nv] = p
                tree_r[p] = v
                tree_r[v] = pp
                tree[pp][p_ind] = v
                tree[v][v_ind] = p
                tree[p][v_ind] = nv
            else:
                dp = tree[p][(tree[p].index(v)+1) % 2]
                nv = tree[v][tree[p].index(v)]
                dv = tree[v][(tree[p].index(v)+1) % 2]
                v_ind = tree[p].index(v)
                tree_r[nv] = p
                tree_r[p] = v
                tree_r.pop(v)
                tree[v][v_ind] = p
                tree[p][v_ind] = nv
                root = v
        else:
            p = tree_r[v]
            if p in tree_r.keys():
                pp = tree_r[p]
                dp = tree[p][(tree[p].index(v)+1) % 2]
                p_ind = tree[pp].index(p)
                v_ind = tree[p].index(v)
                tree_r[p] = v
                tree_r[v] = pp
                tree[pp][p_ind] = v
                tree[v] = [-1, -1]
                tree[v][v_ind] = p
                tree[p][v_ind] = -1
            else:
                dp = tree[p][(tree[p].index(v)+1) % 2]
                v_ind = tree[p].index(v)
                tree_r[p] = v
                tree_r.pop(v)
                tree[v] = [-1, -1]
                tree[v][v_ind] = p
                tree[p][v_ind] = -1
                root = v

def LVR(v):
    if v != -1:
        if v in tree.keys(): LVR(tree[v][0])
        print(v, end=' ')
        if v in tree.keys(): LVR(tree[v][1])

LVR(root)