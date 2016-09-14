# 方法一：使用两个列表
class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        将所有的0保存在另外一个列表中，删除原来列表中所有的0，再把存0的列表加到原列表后面
        """
        zNums = []
        for num in nums:
            if num == 0:
                zNums.append(num)
        for i in range(len(zNums)):
            nums.remove(0)
        nums += zNums


# 方法二：使用两个“指针”
class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        令初始j=0,利用i遍历nums列表，若nums[i]非0，则交换nums[i]与nums[j]；时间复杂度O(n)。
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
