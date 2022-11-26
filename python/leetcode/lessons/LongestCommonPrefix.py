class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ans = ""
        n = min([len(i) for i in strs])
        for i in range(n):
            char = strs[0][i]
            flag = False
            for j in range(1, len(strs)):
                if char != strs[j][i]:
                    char = ''
                    flag = True
                    break
            ans += char
            if flag: break
        return ans