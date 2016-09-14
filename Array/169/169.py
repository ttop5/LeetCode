class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[list]
        :rtype: int
        使用字典统计每一个数字出现的次数然后取出字典中值最大的键
        """
        numsDic = {}
        for x in nums:
            if x in numsDic:
                numsDic[x] += 1
            else:
                numsDic[x] = 1
        return max(numsDic.items(), key=lambda x: x[1])[0]
