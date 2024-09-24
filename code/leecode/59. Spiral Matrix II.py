class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ans=[[0 for _ in range(n)] for _ in range(n)]
        x=0
        y=0
        ans[x][y]=1
        # 右 下 左 上
        for i in range(2,n**2+1):
            
            pass