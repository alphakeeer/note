# 二叉搜索树特点：左子树 < 节点 < 右子树
# 初始思路：从1～n各做root
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.n = 0
        self.root = TreeNode

    def joinList(self, root: int, larr: list[list], rarr: list[list]):
        ans = []
        for i in larr:
            for j in rarr:
                jointList = i+[root]+j
                ans.append(jointList)
        return ans

    def fillInNumber(self, root: int, larr: list, rarr: list) -> list[list]:
        llist=[]
        rlist=[]
        ans=[]
        if rarr is None and larr is None:
            ans.append([root])
        elif larr is not None and rarr is not None:
            for i in range(len(larr)):
                llist.append(self.joinList(larr[i], self.fillInNumber(larr[:i]), self.fillInNumber(larr[i+1:])))
            for i in range(len(rarr)):
                rlist.append(self.joinList(rarr[i], self.fillInNumber(rarr[:i]), self.fillInNumber(rarr[i+1:])))
            ans=self.joinList(root,llist,rlist)
        elif larr is not None and rarr is None:
            
        elif larr is None and rarr is not None:
            return self.joinList(root, [[null]], self.fillInNumber(rarr))

    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        self.n = n
        arr = [i for i in range(1, n+1)]
        for i in range(n):
            root = i+1
            larr = arr[:i]
            rarr = arr[i+1:]
            self.ans.append(self.fillInNumber(root, larr, rarr))
        return self.ans
