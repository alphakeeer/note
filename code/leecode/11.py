class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ans = 0
        while l < r:
            area = (r-l) * \
                height[l] if height[l] < height[r] else (r-l)*height[r]
            if area > ans:
                ans = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans


'''
暴力：
    for l in range(n):
        for r in range(l+1,n):
            s=(r-l)*height[l] if height[l]<height[r] else (r-l)*height[r]
            if s>ans: ans=s
双指针+贪心：
    左右各一指针，每次只移动height较小的一方

'''
