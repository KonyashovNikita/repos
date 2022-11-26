def f(s):
    return sum(s) % 2
    
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        print(s)
        result = list(map(int, s.replace('(', ' ').replace(')', ' ').replace('-', ' ').replace('+', ' ').split()))
        ans = 0
        count_l = 0
        count = 0
        sign = [0] * 10000
        is_negativ = 0
        temp = '0'
        i = 0
        while i < len(s):
            if s[i] == '(':
                count_l += 1
                sign[count_l] = is_negativ
                is_negativ = 0
        
            elif s[i] == ')':
                if temp != '0':
                    ans += (1 - 2 * ((f(sign[:count_l + 1])+is_negativ) % 2)) * result[count]
                    count += 1
                count_l -= 1
                temp = '0'

            elif s[i] == '-':
                if temp != '0' :
                    ans += (1 - 2 * ((f(sign[:count_l + 1])+is_negativ) % 2)) * result[count]
                    count += 1
                temp = '0'
                is_negativ = 1

            elif s[i] == '+':
                if temp != '0':
                    ans += (1 - 2 * ((f(sign[:count_l + 1])+is_negativ) % 2)) * result[count]
                    count += 1
                temp = '0'
                is_negativ = 0

            else:
                temp += s[i]

            i += 1
        if count < len(result):
            ans += (1 - 2 * ((f(sign[:count_l + 1])+is_negativ) % 2)) * result[count]
        return ans
            
s = input()
sol = Solution()
print(sol.calculate(s))