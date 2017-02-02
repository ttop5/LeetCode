# 搜索

## 顺序搜索
顺序或者线性搜索是最基本的算法。它是将每一个数据结构中的元素和我们要的元素进行比较。

```JavaScript
function sequentialSearch(array, item) {
  for (let i=0; i<array.length; i++) {
    if (item === array[i]) {
      return i;
    }
  }
  return -1;
}
```

## 二分查找
这个算法要求被搜索的数据结构已排序。具体步骤：

+ 选择数组的中间值；
+ 如果选中的值是待搜索值，那么算法执行完毕（值找到了）；
+ 如果待搜索值比选中的值小，则返回步骤１并在选中值左边的子数组中寻找；
+ 如果待搜索值比选中的值大，则返回步骤１并在选中值右边的子数组中寻找。

```JavaScript
function binarySearch(array, item){
  let h = array.length - 1;
  let l = 0;
  while (l <= h) {
    let m = Math.floor((h + l) / 2);
    if (array[m] === item) {
      return m;
    }
    if (item > array[m]) {
      l = m + 1;
    } else {
      h = m - 1;
    }
  }
  return -1;
}
```
