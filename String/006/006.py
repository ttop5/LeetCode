# 方法一（超时）：
class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        模拟转变的过程，reduce为一个一元二次函数，operater库提供一些函数方法
        """
        if numRows == 1 or numRows >= len(s):
            return s
        zigzag = [[] for x in range(numRows)]
        row, step = 0, 1
        for x in s:
            zigzag[row] += x
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        print zigzag
        return "".join(reduce(operator.add, zigzag))


# 方法二：
class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        找规律什么的最烦了，还好我不会...
        """
        if numRows == 1 or numRows >= len(s):
            return s
        final = [[] for row in xrange(numRows)]
        for i in range(len(s)):
            final[numRows - 1 - abs(numRows - 1 - i %
                                    (2 * numRows - 2))].append(s[i])
        return "".join(["".join(final[i]) for i in xrange(numRows)])
