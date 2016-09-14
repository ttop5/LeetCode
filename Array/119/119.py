class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        暴力，全部求出来然后再取出想要的行
        """
        numList = []
        for i in range(rowIndex + 1):
            numList.append([1])  # 在列表中生成一个新的列表并将第一个置为1
            for j in range(1, i + 1):
                if i == j:  # 将每个子列表中的最后一个设置为1
                    numList[i].append(1)
                else:
                    numList[i].append(numList[i - 1][j] +
                                      numList[i - 1][j - 1])
        return numList[rowIndex]
