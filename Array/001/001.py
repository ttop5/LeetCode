class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        使用字典将元素和索引的映射关系保存起来，然后相减再进行查找(字典查找效率高)
        """
        numsDic = {}
        nList = []
        L = len(nums)
        for i in range(L):
            numsDic[nums[i]] = i
        # 通过索引遍历而不是通过元素遍历是为了避免出现相同元素而只在字典中存一个的问题如：[0,4,3,0] 0
        for j in range(L):
            # 后面那个条件是为了去除重复项
            if (target - nums[j]) in numsDic and j < numsDic[target - nums[j]]:
                nList.append(j)
                nList.append(numsDic[target - nums[j]])
        return nList
