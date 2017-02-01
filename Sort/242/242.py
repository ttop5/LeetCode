class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        题意：s是否为t字母打乱而构成（即比较两个字符串中的组成元素相同即可）
        """
        return sorted(s) == sorted(t)
