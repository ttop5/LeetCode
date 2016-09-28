/**
 * @param {number[]} digits
 * @return {number[]}
 * 暴力转换测试数组会溢出，唯有模拟是出路啊
 */
function plusOne(digits) {
  for (let i=digits.length-1; i>=0; --i) {
    if (digits[i] != 9) { // 如果该位上的数不是9 那么直接将该位加1就可以了
      digits[i] += 1;
      return digits;
    } else { // 如果该位上的数是9 那么该位加1之后变成了0
      digits[i] = 0;
    }
  }
  // 跳出了for循环说明每一位都是9，那么数组长度不够存放，需要在数组最前面增加一个元素0的项
  digits.splice(0,0,1); // 在digits数组的index为0的地方添加元素1 中间的0代表删除0个元素
  return digits;
}
