from collections import deque
from copy import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def build(data):
        if not data:
            return []
        # data = '['+','.join([str(node) if node is not None else 'None' for node in data]) + ']'
        # dataList = data[1:-1].split(',')
        dataList = [str(node) if node is not None else 'None' for node in data]
        root = TreeNode(int(dataList[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if i >= len(dataList):
                break
            if dataList[i] != 'None':
                node.left = TreeNode(int(dataList[i]))
                queue.append(node.left)
            i += 1
            if i >= len(dataList):
                break
            if dataList[i] != 'None':
                node.right = TreeNode(int(dataList[i]))
                queue.append(node.right)
            i += 1
        return root

    def bfs(self):
        def parse(nodes):
            if not nodes:
                return []
            nxt = []
            now = []
            for node in nodes:
                if not node:
                    continue
                now.append(node.val or None)
                if not node.val:
                    continue
                nxt.append(node.left or None)
                nxt.append(node.right or None)
            now.extend(parse(nxt))
            return now

        result = [self.val]
        result.extend(parse([self.left, self.right]))
        return result


class TreeBuilder:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('None')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        dataList = data[1:-1].split(',')
        root = TreeNode(int(dataList[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if i >= len(dataList):
                break
            if dataList[i] != 'None':
                node.left = TreeNode(int(dataList[i]))
                queue.append(node.left)
            i += 1
            if i >= len(dataList):
                break
            if dataList[i] != 'None':
                node.right = TreeNode(int(dataList[i]))
                queue.append(node.right)
            i += 1
        return root


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def build(self, vals):
        now = None
        while vals:
            now = ListNode(vals.pop(), now)
        self.val = now.val
        self.next = now.next

    def __str__(self):
        stack = [self.val]
        tmp = self.next
        while tmp:
            stack.append(tmp.val)
            tmp = tmp.next
        return str(stack)