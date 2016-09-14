class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        L = ['1']
        if n == 1:
            return '1'
        else:
            for i in range(n - 1):
                j = 0
                while j < len(L):
                    x = L[j]
                    count = 1
                    if j + count == len(L):
                        L[j:j + 1] = ['1', x]
                    else:
                        while j + count < len(L) and L[j + count] == x:
                            count = count + 1
                        L[j:j + count] = [str(count), x]
                    j = j + 2
        return ''.join(L)

s = Solution()
print(s.countAndSay(9))
