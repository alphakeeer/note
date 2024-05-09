# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         ans = 0
#         win = []
#         for ch in s:
#             index=-1
#             for i in range(len(win)):
#                 if win[i]==ch:
#                     index=i

#             if index==-1:
#                 win.append(ch)
#                 if len(win) > ans:
#                     ans = len(win)
#             else:
#                 win=win[index+1:]
#                 win.append(ch)
#         return ans
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,ans=0,0
        win=set()
        cur=0
        for ch in s:
            cur+=1
            while ch in win:
                win.remove(s[l])
                l+=1
                cur-=1
            ans=max(ans,cur)
            win.add(ch)
        return ans
    