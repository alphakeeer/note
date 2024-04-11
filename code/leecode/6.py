class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:                             #正常遍历
            res[i] += c                         #并入字符
            if i == 0 or i == numRows - 1:      #到达转折点进行转向
                flag = -flag
            i += flag
        return "".join(res)
