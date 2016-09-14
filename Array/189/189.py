# 方法一：
class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        LeetCode上报错的数据（[1,2],1）在本地没有问题啊，擦
        """
        nList = []
        i = len(nums) - k
        while i < (len(nums)):
            nList.append(nums[i])
            i += 1
        for j in range(len(nums) - k):
            nList.append(nums[j])
        nums = nList


# 方法二：
class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        和上面方法思路一样，只是巧妙利用列表切片
        """
        L = len(nums)
        if k > 0 and L > 1:
            nums[:] = nums[L - k:] + nums[:L - k]
