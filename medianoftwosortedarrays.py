#median of two sorted arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        f = nums1 + nums2
        f.sort()
        mid = len(f)//2 
        if len(f)%2==0:
            return (f[mid-1]+f[mid])/2 
        else:
            return f[mid]