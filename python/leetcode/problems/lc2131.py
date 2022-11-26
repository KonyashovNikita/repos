class Solution:
    def longestPalindrome(self, words: list) -> int:
        reversable = 0
        polindrom = 0
        words_dict = {}
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1
        for word in words_dict.keys():
            word_rev = word[::-1]
            if word_rev == word:
                reversable += (words_dict[word] // 2) * 4
                polindrom = max(polindrom, (words_dict[word] % 2) * 2)
            elif word_rev in words_dict:
                reversable += min(words_dict[word], words_dict[word_rev]) * 2
        return reversable + polindrom

sol = Solution()
print(sol.longestPalindrome(["ab","ty","yt","lc",'gg', 'ff', 'ff', "cl","ab"]))
