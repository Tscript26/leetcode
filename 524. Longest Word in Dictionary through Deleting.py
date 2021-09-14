"""
Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

 

Example 1:

Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
Example 2:

Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"
 

Constraints:

1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s and dictionary[i] consist of lowercase English letters.
"""
from src import *


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        word_dict = {word: 0 for word in dictionary}
        max_word = ""
        for i in range(len(s)):
            character = s[i]
            for key, value in word_dict.items():
                if value >= len(key):
                    continue
                if key[value] == character:
                    if value <= len(key):
                        word_dict[key] += 1
                    if word_dict[key] == len(key):
                        if len(key) > len(max_word):
                            max_word = key
                        elif len(key) == len(max_word):
                            max_word = sorted([max_word, key])[0]
        return max_word




if __name__ == '__main__':
    S = Solution()
    s = "bab"
    dictionary = ["ba","ab","a","b"]
    start = time.time()
    word = S.findLongestWord(s, dictionary)
    print(time.time() -start)
    print(word)
