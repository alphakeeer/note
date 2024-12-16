# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        def _build(preorder: list[int], inorder: list[int]) -> TreeNode:
            if preorder == []:
                return None
            node = TreeNode(preorder[0])
            node_idx_in = inorder.index(node.val)
            left_pre = preorder[1:1+node_idx_in]
            right_pre = preorder[1+node_idx_in:]
            node.left = _build(left_pre, inorder[:node_idx_in])
            node.right = _build(right_pre, inorder[node_idx_in+1:])
            return node
        return _build(preorder,inorder)

sol=Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(sol.buildTree(preorder,inorder))
def printTree(node: TreeNode, level=0, label="."):
    prefix = " " * (level * 4) + label + ": "
    print(prefix + str(node.val) if node else prefix + "None")
    if node:
        if node.left or node.right:
            printTree(node.left, level + 1, "L")
            printTree(node.right, level + 1, "R")

root = sol.buildTree(preorder, inorder)
printTree(root)