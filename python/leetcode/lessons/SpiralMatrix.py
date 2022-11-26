class Solution:
    def spiralOrder(self, matrix):
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        ind_row = 0
        ind_col = 0
        vector = 0
        check_matrix = [[-1 if (i)%(n+1) == 0 or (j)%(m+1) == 0 else 0 for i in range(n+2)] for j in range(m+2)]
        for _ in range(m * n):
            ans.append(matrix[ind_row][ind_col])
            check_matrix[ind_row+1][ind_col+1] = -1
            if vector == 0:
                if check_matrix[ind_row+1][ind_col+2] == -1:
                    vector = 1
                    ind_row += 1
                else:
                    ind_col += 1
            elif vector == 1:
                if check_matrix[ind_row+2][ind_col+1] == -1:
                    vector = 2
                    ind_col -= 1
                else:
                    ind_row += 1
            elif vector == 2:
                if check_matrix[ind_row+1][ind_col] == -1:
                    vector = 3
                    ind_row -= 1
                else:
                    ind_col -= 1
            elif vector == 3:
                if check_matrix[ind_row][ind_col+1] == -1:
                    vector = 0
                    ind_col += 1
                else:
                    ind_row -= 1
        return ans

sol = Solution()
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
