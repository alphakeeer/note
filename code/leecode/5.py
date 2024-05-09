class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen, n = 0, len(s)
        ans = s[0]

        for i in range(1, n):
            l, r = i-1, i+1
            cur = 1
            while l >= 0 and r < n and s[l] == s[r]:
                cur += 2
                l -= 1
                r += 1
            if cur >= maxlen:
                maxlen = cur
                ans = s[l+1:r]

            l, r = i-1, i
            cur = 0
            while l >= 0 and r < n and s[l] == s[r]:
                cur += 2
                l -= 1
                r += 1
            if cur >= maxlen:
                maxlen = cur
                ans = s[l+1:r]

        return ans
        # res = ''
        # for i in range(len(s)):
        #     start = max(i - len(res) -1, 0)
        #     temp = s[start: i+1]
        #     if temp == temp[::-1]:
        #         res = temp
        #     else:
        #         temp = temp[1:]
        #         if temp == temp[::-1]:
        #             res = temp
        # return res
