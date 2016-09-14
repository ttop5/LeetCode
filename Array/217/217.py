# 方法一：
class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        先排序，然后循环比较列表中相邻的两个数的大小
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


# 方法二：
class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        使用集合存储遍历过的元素，之后每遍历一个元素就查找集合中有没有
        不使用列表的原因是列表比集合查找效率低，会超时
        """
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False
