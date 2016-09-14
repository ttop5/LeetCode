class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        先转换成十进制相加再转换成二进制输出。
        int()方法能将其他进制转换成十进制，转换出来是数字；
        bin()方法能将十进制转换成二进制，转换出来是字符串而且前面多了'0b'这两个字符。
        """
        return bin(int(a, 2) + int(b, 2))[2:]
