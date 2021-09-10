from collections import deque
from copy import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def build(ns):
        nodes = copy(ns)
        if not nodes:
            return None
        head = TreeNode(nodes.pop(0))
        stack = [head]
        no_left = False
        while nodes:
            now = stack.pop(0)
            nxt = nodes.pop(0)
            if not now:
                nodes.pop(0)
                continue
            if not now.left and not no_left:
                if nxt is None:
                    no_left = True
                now.left = TreeNode(nxt) if nxt is not None else None
                stack.append(now)
                stack.append(now.left)
                continue
            if not now.right:
                now.right = TreeNode(nxt)
                stack.append(now.right)
            no_left = False
        return head

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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
