class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        使用split()先将字符串分割成列表，去除列表中空元素，然后对处理出来的列表作判断和返回
        """
        sList = s.split(" ")
        while '' in sList:
            sList.remove('')
        if len(sList) != 0:
            if len(sList) == 1:
                return len(sList[0])
            else:
                return len(sList[len(sList) - 1])
        else:
            return 0
