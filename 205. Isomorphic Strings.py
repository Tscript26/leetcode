"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""
from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}
        if not s or not t:
            return False
        if len(s) != len(t):
            return False
        i = 0
        while i < len(t):
            if s[i] not in s_d.keys():
                s_d[s[i]] = t[i]
            else:
                if s_d[s[i]] != t[i]:
                    return False
            if t[i] not in t_d.keys():
                t_d[t[i]] = s[i]
            else:
                if t_d[t[i]] != s[i]:
                    return False
            i += 1
        return True
# s = "badc"
# t = "badc"
s = f"foo{'t' * 4000}"
t = f"baa{'m' * 4000}"
S = Solution()
print(S.isIsomorphic(s, t))
