"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,None,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,None,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

"""
from src import *
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, mx):
            if not root: return 0
            mx, val = (root.val, 1) if root.val >= mx else (mx, 0)
            return dfs(root.left, mx) + dfs(root.right, mx) + val
        return dfs(root, -float('inf'))

        res = 0
        def dfs(root, mx):
            nonlocal res
            if root:
                if root.val >= mx:
                    res += 1
                    mx = root.val
                dfs(root.left, mx)
                dfs(root.right, mx)
        dfs(root, -float('inf'))
        return res
S = Solution()
a = TreeNode.build([-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3])
# a = TreeNode(1, TreeNode(3,TreeNode(4),TreeNode(2)))
print(a.bfs())
print(S.goodNodes(a))
print(float('-inf') < -10000)

