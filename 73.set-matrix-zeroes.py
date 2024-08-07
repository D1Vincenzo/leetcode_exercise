#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix(0))
        z_row, z_col = [], []
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    z_row.append(i)
                    z_col.append(j)
        
        for i in range(z_row):
            for j in range(col):
                matrix[i][j] = 0
                
        for i in range(z_col):
            for j in range(row):
                matrix[i][j] = 0
# @lc code=end

