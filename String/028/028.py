class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        用in判断是否为子串（因为index如果不是子串会由异常），然后在求子串的位置
        """
        if needle in haystack and haystack.index(needle) >= 0:
            return haystack.index(needle)
        else:
            return -1
