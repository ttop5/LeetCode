class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        理解：m只是用于告之developer当前nums1数组中只有前m个元素有意义. 同理n之于nums2.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
