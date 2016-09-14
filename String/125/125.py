class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        将字符串转换成列表然后进行处理剩下数字和字母，翻转然后再进行对比
        """
        sList = list(s.lower())
        L = []
        for x in sList:
            if x.isalpha() or x.isdigit():
                L.append(x)
        print L
        if L == [] or L == L[::-1]:
            return True
        else:
            return False
