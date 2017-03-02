# 字符串

JS的字符串是不可变的(immutable)，String类定义的方法都不能改变字符串的内容，这些方法返回的是全新的字符串，而不是修改原始的字符串。

## 常用字符串方法

| 方法名 | 描述 |
| ----- | -----|
| concat | 将两个或者多个字符串组合起来 |
| replace | 字符串替换 |
| toLowerCase | 转换成小写 |
| toUpperCase | 转换成大写 |
| length | 返回字符串的长度 |
| substring | 返回字符串的一个子串，传入的参数是起始位置和结束位置 |
| substr | 返回一个字符串，传入的参数是起始位置和长度 |
| slice | 提取字符串的一部分，并返回一个新的子串 |
| split | 通过将字符串划分成子串，将一个字符串做成字符串数组 |

## ES6新增方法

| 方法名 | 描述 | 基本示例 |
| ----- | -----| ----- |
| for...of | 字符的遍历接口 | for (let item of 'foo') { console.log(item); } |
| at() | 字符串的位置内容的搜索 | 'abcd'.ChartAt(2); |
| indexOf() | 返回被包含的字符串的位置 |  |
| include() | 返回布尔值，表示是否找到了参数的字符串 |  |
| startsWith() | 返回布尔值，表示是否在源字符串的头部 |  |
| endsWith() | 返回布尔值，表示是否在源字符串的尾部 |  |
| repeat() | 重复 | 'na'.repeat(2); |
| padStart() | 用于补全头部 | 'x'.padStart(5, 'ab') |
| padEnd() | 用于尾部补全 | 'x'.padEnd(5, 'ab') |
