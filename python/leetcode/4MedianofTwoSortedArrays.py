# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        arrlen = len(arr)
        if arrlen % 2 is 1:
            return arr[arrlen // 2]
        else:
            return (arr[arrlen // 2] + arr[arrlen // 2 - 1]) / 2