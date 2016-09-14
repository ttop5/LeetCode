class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        循环遍历数组，统计min(引用次数x, 剩余文章篇数L-i)的最大值
        """
        L = len(citations)
        for i,x in enumerate(sorted(citations)):
            if L-i <= x:
                return L-i
        return 0
