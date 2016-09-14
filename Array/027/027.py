class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        循环判断，一直删除到没有（因为remov方法每次只会删除第一个）
        """
        while val in nums:
            nums.remove(val)
        return len(nums)
