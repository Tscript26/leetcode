"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from src import *


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        direcs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # 构建字典树
        Trie = defaultdict(dict)
        for word in words:
            Trie = self.insert_word(Trie, word)
        # 回溯搜索
        visited = [[0] * n for _ in range(m)]
        ans = []

        # (i,j) board中的横纵坐标
        # 返回： 当board[i][j]在letternode.key()中时 是否能匹配成功
        def dfs(i, j, letter_node):
            # letters_next是board[i][j]匹配之后下面的可选字符
            # 如果出现终止符# 则说明 board[i][j]是一个单词的结束
            letters_next = letter_node[board[i][j]]
            ending = letters_next.pop('#', False)
            print(ending)
            if ending:
                ans.append(ending)
            # 下面继续寻找board[i][j]接上邻居字符是否能继续匹配
            for di, dj in direcs:
                i1, j1 = i + di, j + dj
                if 0 <= i1 < m and 0 <= j1 < n and visited[i1][j1] == 0 and board[i1][j1] in letter_node[board[i][j]]:
                    visited[i1][j1] = 1

                    dfs(i1, j1, letter_node[board[i][j]])

                    visited[i1][j1] = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] in Trie:
                    visited[i][j] = 1
                    dfs(i, j, Trie)
                    visited[i][j] = 0
        return ans

    # 向字典树中插入单词word
    def insert_word(self, Trie, word):
        cur_level = Trie
        for c in word:
            if c not in cur_level:
                cur_level[c] = defaultdict(dict)
            cur_level = cur_level[c]
        cur_level['#'] = word
        return Trie


if __name__ == '__main__':
    S = Solution()
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath",
             "pea",
             "eat",
             "rain"]
    res = S.findWords(board, words)
    print(res)
