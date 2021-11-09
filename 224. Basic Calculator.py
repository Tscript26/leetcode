"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.

"""


class Solution:
    def calculate(self, s: str) -> int:
        ops = [1]
        sign = 1

        ret = 0
        n = len(s)
        i = 0
        while i < n:
            print(ret, ops, sign, s[i])
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ret += num * sign
        return ret

    def calculate2(self, s: str) -> int:
        chrs = [c for c in list(s) if c != ' ']
        inner = False
        pre = None
        stack = []
        def temp():
            nonlocal chrs
            stack = []
            pre = ""
            while chrs:
                now = chrs.pop(0)
                if now == "(":
                    res = temp()
                    stack.append(res)
                if not now.isdigit():
                    if pre:
                        stack.append(pre)
                        pre = ""
                else:
                    pre += now
                if now == ")":
                    print(stack)
                    return cal(stack)
                if now in "+-":
                    stack.append(now)
            if pre:
                stack.append(pre)
                pre = ""
            if stack:
                return cal(stack)
            return 0
        def cal(stack):
            pre = None
            final = 0
            for s in stack:
                s = str(s)
                if s in "+-":
                    pre = s
                else:
                    now = s
                    if pre:
                        now = str(int(pre + "1") * int(now))
                        pre = None
                    final += int(now)
            return final

        return temp()
if __name__ == '__main__':
    S = Solution()
    s = "(1+(4+5+2) -3)+(6 +8)"
    s = " 2-1 + 2 "
    s = "(1+(-4+5+2) -3)-(6-8)"
    res = S.calculate(s)
    print(res)