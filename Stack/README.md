# 栈
栈是一种后进先出原则的有序集合。新添加或者待删除的元素都保存在栈的末尾，称作栈顶；另一端就叫做栈底。

## 栈的创建

```JavaScript
function Stack() {
  const items = [];
  // 添加
  this.push = function(element) {
    items.push(element);
  };
  // 移除
  this.pop = function() {
    return items.pop();
  };
  // 栈顶元素
  this.peek = function() {
    return items[items.length-1];
  };
  // 是否为空栈
  this.isEmpty = function() {
    return items.length === 0;
  };
  // 清空栈
  this.clear = function() {
    items = [];
  };
  // 元素个数
  this.size = function() {
    return items.length;
  };
  // 打印
  this.print = function() {
    console.log(items.toString());
  };
}
```

## 栈类的使用

```JavaScript
const stack = new Stack();
stack.isEmpty();  // true

stack.push(5);
stack.push(8);
stack.peek();  // 8

stack.push(11);
stack.size();  // 3
stack.isEmpty();  // false

stack.pop();
stack.print();  // [5, 8]
```

## 栈的应用实例

### 进制转换

### 括号匹配

### 汉诺塔
