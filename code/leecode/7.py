class Solution:
    def reverse(self, x: int) -> int:
        '''
        -2147483648
        2147483647
        '''
        if -10<x<10:
            return x
        sx=str(x)
        if sx[0]!="-":
            sx=sx[::-1]
            x=int(sx)
        else:
            sx=sx[:0:-1]
            x=int(sx)
            x=-x
        return x if -2147483648 < x < 2147483647 else 0

        y,res=ans(x),0
        boundry=(1<<31)-1 if x>0 else 1<<31
        while y!=0:
            res=res*10+y%10
            if res<boundry:
                return 0
            y//=10
        return res if x>0 else -res
            