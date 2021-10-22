"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""

from src import *


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = list()
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord("a")
                if ((mask >> idx) & 1):  # // 若 mask 已有 ch，则说明 s 含有重复字母，无法构成可行解
                    mask = 0
                    break
                mask |= 1 << idx  # 将 ch 加入 mask 中
            if mask > 0:
                masks.append(mask)
        ans = 0

        def backtrack(pos: int, mask: int) -> None:
            if pos == len(masks):
                nonlocal ans
                ans = max(ans, bin(mask).count("1"))
                return
            print(bin(masks[pos]), bin(mask))
            if (mask & masks[pos]) == 0:  # mask 和 masks[pos] 无公共元素
                backtrack(pos + 1, mask | masks[pos])
            backtrack(pos + 1, mask)

        backtrack(0, 0)
        return ans


if __name__ == '__main__':
    S = Solution()
    arr = ["cha","r","act","ers"]
    res = S.maxLength(arr)
    print(res)

