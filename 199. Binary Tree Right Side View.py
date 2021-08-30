"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []

"""
from src import *


class Solution:

    def rightSideView2(self, root: TreeNode) -> List[int]:
        """
        BFS
        :param root:
        :return:
        """
        result = [root.val]
        pre = [root]
        while pre:
            tmp = []
            while pre:
                now = pre.pop(0)
                if not now:
                    continue
                left = now.left
                right = now.right
                tmp.append(left)
                tmp.append(right)
            if tmp:
                # print([node.val for node in tmp if node])
                for node in tmp[::-1]:
                    if node and node.val:
                        result.append(node.val)
                        break
            pre = tmp
        return result




if __name__ == '__main__':
    S = Solution()
    b = TreeNode.build([1, 2, 7, 4, None, 6, None])
    # print(b.bfs())
    res = S.rightSideView(b)
    print(res)