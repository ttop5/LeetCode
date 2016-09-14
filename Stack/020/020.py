class Solution(object):

    def isValid(self, s,):
        """
        :type s: str
        :rtype: bool
        使用字典存储括号对，使用列表模拟栈
        """
        stack = []
        dict = {")":"(", "]":"[", "}":"{"}
        for x in s:
            if x in dict.values():
                stack.append(x)
            elif x in dict.keys():
                if stack == [] or dict[x] != stack.pop():
                    return False
        return stack == []
