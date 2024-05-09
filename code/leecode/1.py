class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        for i, val in enumerate(nums):
            if target-val in ans:
                return [ans[target-val],i]
            else:
                ans[val]=i
        return []