class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        先把列表转换成数字，数字加1，得到的结果再转换成最终列表。数字和列表之间的转换要先转换成字符
        """
        num = int("".join([str(i) for i in digits]))
        num += 1
        resultList = [int(j) for j in str(num)]
        return resultList
