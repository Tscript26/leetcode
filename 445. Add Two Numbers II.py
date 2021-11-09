"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 

Follow up: Could you solve it without reversing the input lists?

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from src import *
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t1 = l1
        t2 = l2
        while t1 and t2:
            t1 = t1.next
            t2 = t2.next
        if not t1:
            left = t2
            other = l1
            head = l2
        else:
            left = t1
            other = l2
            head = l1
        nxt = head
        if not t1 and not t2:
            pass
        else:
            while left:
                left = left.next
                nxt = nxt.next
        while other:
            nxt.val += other.val
            nxt = nxt.next
            other = other.next
        modified= True
        while modified:
            modified=False
            check = head
            pre = None
            while check:
                if check.val >= 10:
                    modified = True
                    upper = 0
                    while check.val >= 10:
                        check.val -= 10
                        upper += 1
                    if not pre:
                        head = ListNode(upper, check)
                    else:
                        pre.val += upper
                else:
                    pre = check
                    check = check.next
        return head

if __name__ == '__main__':
    l1 = [7,2,4,3]
    l2 = [5,6,4]
    t1 = ListNode()
    t1.build(l1)
    t2 = ListNode()
    t2.build(l2)
    S = Solution()
    print(S.addTwoNumbers(t1, t2))


