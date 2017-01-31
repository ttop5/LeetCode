# 122. Best Time to Buy and Sell Stock II

## 题目大意：

> 用一个数组表示股票每天的价格，数组的第i个数表示股票在第i天的价格。求最大的收益（可以进行多次交易）。

## 解题思路：

> 从头到尾扫描prices，如果price[i] – price[i-1]大于零则计入最后的收益中，即贪心法。
