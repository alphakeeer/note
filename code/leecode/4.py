class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        nums1[n:]=nums2
        n=len(nums1)
        nums1=sorted(nums1)
        if n%2==1:
            ans=nums1[n//2]
        else:
            ans=(nums1[n//2]+nums1[n//2-1])*0.5
        return ans
            