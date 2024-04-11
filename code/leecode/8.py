class Solution:
    def myAtoi(self, s: str) -> int:
        nums=[0,1,2,3,4,5,6,7,8,9]
        sindex=-1#record if record num
        eindex=-1
        posflag=True#record if num is positive
        for i,ch in enumerate(s):
            if  sindex==-1:
                if ch==' ':
                    continue
                elif ch=='-':
                    posflag=False
                    sindex=i+1
                elif ch in nums:
                    sindex=i
                else:
                    return
            else:
                if ch not in nums:
                    eindex=i
                    break
                else:
                    continue
        num=int(s[sindex:eindex])
        boundry=(1<<31)-1 if posflag else 1<<31
        if num>=boundry:
            return boundry if posflag else -boundry
        return num if posflag else -num
