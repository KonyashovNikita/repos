class Solution:
    def findBall(self, grid):
        ans = []
        m = len(grid)
        n = len(grid[0])
        for i in range(n):
            col = i
            for j in range(m):
                cur_v = grid[j][col]
                if (col == n-1 and cur_v == 1) or (col == 0 and cur_v == -1) or cur_v * grid[j][col+cur_v] == -1:
                    col = -1
                    break
                col += cur_v
            ans.append(col)
        return ans
sol = Solution()
print(sol.findBall([[-1]]))
