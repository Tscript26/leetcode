"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0


Constraints:

rows == matrix.length
cols == matrix[i].length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.


"""

from src import *
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        res = 0
        heights = [0 for _ in range(len(matrix[0]) + 1)]
        for row in matrix:
            for i in range(len(row)):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            now = [0] + heights + [0]
            stack = [0]

            for i in range(1, len(now)):
                while now[i] < now[stack[-1]]:
                    cur_height = now[stack.pop()]
                    cur_width = i - stack[-1] - 1
                    res = max(res, cur_height * cur_width)
                stack.append(i)
        return res


if __name__ == '__main__':
    S = Solution()
    import numpy as np

    matrix = [[str(i) for i in np.random.randint(0, 2, 200)] for _ in range(200)]
    print(S.maximalRectangle(matrix))
