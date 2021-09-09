"""
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
"""

from src import *
# Definition for singly-linked list.

class Solution:
    """
    需要注意的点：
    1. 列表长度的奇偶
    2. 长度为2时的特殊处理
    """
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        due = False
        while fast.next:
            if not fast.next.next:
                # 偶数
                due = True
                break
            else:
                fast = fast.next.next
            slow = slow.next
        if due and slow.next:
            slow = slow.next
        def reverse(r_t):
            tmp = r_t
            pre = None
            while tmp:
                nxt = tmp.next
                tmp.next = pre
                pre = tmp
                tmp = nxt
            return pre
        rev = reverse(slow)
        while rev:
            if rev.val == head.val:
                rev = rev.next
                head = head.next
            else:
                return False
        return True


tmp = [1,2]
a = ListNode(tmp.pop())
while tmp:
    a = ListNode(tmp.pop(), a)


S = Solution()
print(S.isPalindrome(a))
