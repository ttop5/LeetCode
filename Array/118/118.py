class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        第一个和最后一个置为1，其他的等于[i-1][i]+[i-1][j-1]
        """
        numList = []
        for i in range(numRows):
            numList.append([1])  # 在列表中生成一个新的列表并将第一个置为1
            for j in range(1, i + 1):
                if i == j:  # 将每个子列表中的最后一个设置为1
                    numList[i].append(1)
                else:
                    numList[i].append(numList[i - 1][j] +
                                      numList[i - 1][j - 1])
        return numList
