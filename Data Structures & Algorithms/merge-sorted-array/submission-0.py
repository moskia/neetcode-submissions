class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m, n
        k = m + n - 1
        while i > 0 and j > 0:
            if nums1[i-1] < nums2[j-1]:
                nums1[k] = nums2[j-1]
                k -= 1
                j -= 1
            else: 
                nums1[k] = nums1[i-1]
                nums1[i-1] = 0
                k -= 1
                i -= 1

        if (j > 0): nums1[:j] = nums2[:j]