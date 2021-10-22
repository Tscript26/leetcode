"""
Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 10^5
s[i] is a printable ascii character.
 

Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
from src import *
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        i = 0
        j = l -1
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i+=1
            j-=1