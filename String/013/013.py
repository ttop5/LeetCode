class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        不会罗马数字（懵逼脸）
        """
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        L = len(s)
        num = 0
        for i in range(L - 1):
            if dic[s[i]] >= dic[s[i + 1]]:
                num += dic[s[i]]
                print "s[i]=", dic[s[i]]
                print num
            else:
                num -= dic[s[i]]
        num += dic[s[L - 1]]
        return num
