# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  # 循环做法
    def __init__(self) -> None:
        self.ans = []

    def foo(self, root: Optional[TreeNode]):
        if root.left != None:
            self.foo(root.left)
        self.ans.append(root.val)
        if root.right != None:
            self.foo(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 中序访问：左中右
        if root != None:
            self.foo(root)
        return self.ans



class Solution: #迭代解法
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        current = root
        ans = []

        while current is not None or stack:
            # 一路探到最左点，并将途中点压入栈
            while current is not None:
                stack.append(current)
                current = current.left
            
            # 压入当前栈顶数据并变更为右点
            current = stack.pop()
            ans.append(current.val)
            current = current.right

        return ans
