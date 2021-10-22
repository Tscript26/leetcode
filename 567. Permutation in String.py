"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

"""
from src import *
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        stack_s1 = Counter([s for s in s1])
        for i in range(len(s2)):
            if s2[i] in stack_s1:
                tmp = [s for s in s2[i:i+len(s1)]]
                if Counter(tmp) == stack_s1:
                    return True
        return False



if __name__ == '__main__':
    s1 = "abc"
    s2 = "bbbca"
    S = Solution()
    res = S.checkInclusion(s1, s2)
    print(res)