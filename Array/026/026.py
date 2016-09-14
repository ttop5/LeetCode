class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        用一个列表将需要删除的值存起来，然后遍历一次进行删除
        """
        nList = []
        if len(nums) > 1:
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    nList.append(nums[i])
            for x in nList:
                nums.remove(x)
        return len(nums)
