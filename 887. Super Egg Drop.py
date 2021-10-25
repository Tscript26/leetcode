"""
887. Super Egg Drop
You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.



Example 1:

Input: k = 1, n = 2
Output: 2
Explanation:
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.
Example 2:

Input: k = 2, n = 6
Output: 3
Example 3:

Input: k = 3, n = 14
Output: 4


Constraints:

1 <= k <= 100
1 <= n <= 104
"""


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        def cal_f(k, t):
            if t == 0 or k == 1:
                return t + 1
            return cal_f(k - 1, t - 1) + cal_f(k, t - 1)

        t = 1
        while cal_f(k, t) < n:
            t += 1
        return t

    def superEggDrop2(self, k: int, n: int) -> int:
        """
        DP
        :param k:
        :param n:
        :return:
        """

        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    # 只剩一个鸡蛋只能从下往上一个一个试
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 x values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
                                  for x in (lo, hi))
                memo[k, n] = ans
            return memo[k, n]

        return dp(k, n)

    def superEggDrop3(self, k, n):
        memo = {}
        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo,hi = 0, n
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k -1, x -1)
                        t2 = dp(k, n - x)
                        if t1 > t2:
                            hi = x
                        elif t1 < t2:
                            lo = x
                        else:
                            lo = hi = x
                    ans = 1 + min(max(dp(k - 1, x -1), dp(k, n - x))for x in (lo, hi))
                memo[k, n] = ans
            return memo[k, n]
        return dp(k,n)

if __name__ == '__main__':
    S = Solution()
    k, n = 2, 100
    res = S.superEggDrop3(k, n)
    print(res)
    res = S.superEggDrop(k, n)
    print(res)
