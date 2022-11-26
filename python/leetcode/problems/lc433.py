from copy import copy
def is_min_change(str1, str2):
    k = 0
    for i in range(8):
        if str1[i] != str2[i]:
            k += 1
    return k == 1

def find_gen(startgene, endgene, tree, check):
    if startgene == endgene:
        return 0 
    ans = []
    check[endgene] = -1
    for gen in tree[endgene]:
        if check[gen] != -1:
            cur_count = find_gen(startgene, gen, tree, copy(check))
            if cur_count != -1:
                ans.append(cur_count + 1)
    if ans:
        return min(ans)
    return -1

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank = bank + [startGene]
        ckeck = {i:0 for i in bank}
        if endGene in bank:
            tree = {}
            for gen1 in bank:
                tree[gen1] = []
                for gen2 in bank:
                    if is_min_change(gen1, gen2):
                        tree[gen1].append(gen2)
            return find_gen(startGene, endGene, tree, copy(ckeck))
        else:
            return -1
        


sol = Solution()
print(sol.minMutation("AAAACCCC","CCCCCCCC",["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]))
