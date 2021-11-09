

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        strs = "".join([chr(ord('A') + i) for i in range(26)])
        stack = 0
        for c in list(columnTitle):
            stack *= 26
            stack += strs.index(c) + 1
        return stack
S = Solution()
print(S.titleToNumber("FXSHRXW"))# 2147483647