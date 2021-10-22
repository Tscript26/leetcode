"""
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

 

Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"
 

Constraints:

-231 <= num <= 231 - 1

"""

class Solution:
    def toHex(self, num: int) -> str:
        stack = []
        trans = "01234567789abcdef"
        reverse = False
        if num < 0:
            reverse = True
            num = -num
        while num:
            left = num //16
            right = num % 16
            num = num //16
            stack.append(right)
        if reverse:
            while len(stack) < 8:
                stack.append(0)
            for i in range(len(stack)):
                stack[i] = 16 - stack[i]
                if i == 0:
                    stack[i] += 1
        print(stack)
        return ''.join(trans[n] for n in stack[::-1])
        return str(hex(num)[2:])


if __name__ == '__main__':
    S = Solution()
    num = 26
    print(str(hex(num)))
    res = S.toHex(num)
    print(res)