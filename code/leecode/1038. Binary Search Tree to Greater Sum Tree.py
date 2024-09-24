# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 迭代解法
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur = root
        stack = []
        val = 0
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur.val += val
            val = cur.val
            cur = cur.left
        return root


class Solution:  # 递归解法 faster
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.right)
            node.val += self.total
            self.total = node.val
            dfs(node.left)
        dfs(root)
        return root
