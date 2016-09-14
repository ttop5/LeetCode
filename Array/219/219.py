class Solution(object):
    
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        使用字典存储遍历过的元素和元素的索引,每遍历一次查询字典中有没有这个数
        如果有就说明有重复的数，再比较|i-j| <= k这个条件;如果没有就存入字典
        """
        numDic = {}
        for i in range(len(nums)):
            if nums[i] in numDic:
                j = numDic[nums[i]]
                if abs(i-j) <= k:
                    return True
            numDic[nums[i]] = i
        return False
