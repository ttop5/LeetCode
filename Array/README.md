# 数组
几乎所有的编程语言都原生支持数组类型，因为数组是最简单的内存数据结构。

## 添加和删除元素
+ 添加到末尾：push
+ 添加到首位：unshift
+ 删除末尾元素：pop
+ 删除首位元素: shift

> 通过push和pop方法，可以使用数组来模拟`栈`；使用shift和unshift来模拟`队列`。

## 二维和多维数组
以二维数组为例，初始化：
```JavaScript
const array = [];
array[0] = [01, 02, 03, 04, 05];
array[1] = [11, 12, 13, 14, 15];
```
遍历数组：
```JavaScript
function printArray(array) {
  for (let i=0; i<array.length; i++) {
    for (let j=0; j<array[i].length; j++) {
      cnsole.log(array[i][j]);
    }
  }
}
```

## 数组方法参考
在JS里，数组是可修改的对象。

| 方法名 | 描述 |
| ----- | ----- |
| concat | 链接2个或者多个数组，并返回结果 |
| every | 对数组的每一项运行给定的函数，如果该函数对每一项都返回true，则返回true |
| filter | 对数组总的每一项运行给定函数，返回该函数会返回true的项组成的数组 |
| forEach | 对数组中的每一项运行给定的函数。这个方法没有返回值 |
| join | 将所有的数组元素连接成一个字符串 |
| indexOf | 返回第一个与给定参数相等的数组元素的索引，没有找到则返回-1 |
| lastIndexOf | 返回在数组中搜索到的与给定参数相等的元素的索引里最大的值 |
| map | 对数组中的每一项运行给定的函数，返回每次函数调用的结果组成的数组 |
| reverse | 颠倒数组中元素的顺序，第一个与最后一个元素交换位置，其他类似 |
| slice | 传入索引值，将数组里对应索引范围内的元素作为新的数组返回 |
| some | 对数组中的每一项运行给定函数，如果任一向返回true，则返回true |
| sort | 按照字母顺序对数组进行排序，支持传入指定排序方法的函数作为参数 |
| toString | 将数组作为字符串返回 |
| valueOf | 和toString一样，将数组作为字符串返回 |

> 附： [sort函数自定义排序](https://github.com/ttop5/blog/issues/18)
