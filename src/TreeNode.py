class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def build(nodes):
        if not nodes:
            return None
        root = TreeNode(nodes.pop(0))
        pre = [root]
        now = []
        nxt = []
        while nodes:
            while pre:
                node = pre.pop(0)
                if nodes:
                    node.left = TreeNode(nodes.pop(0))
                    nxt.append(node.left)
                if nodes:
                    node.right = TreeNode(nodes.pop(0))
                    nxt.append(node.right)
            pre = nxt
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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next