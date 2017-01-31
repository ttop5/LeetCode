/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
// 方法一：(答案正确，但是不通过)
 function rotate(nums, k) {
   if (k !== 0) {
     const len = nums.length;
     let newArray1 = nums.splice(len-1-k, len-1);
     const newArray2 = nums.concat(newArray1);
     nums = newArray2;
   }
 }

// 方法二：
function rotate(nums, k) {
  k %= nums.length;
  let tmp = [];
  if (k) {
    tmp = nums.slice(-k);
  }
  nums.splice(-k, k);
  Array.prototype.unshift.apply(nums, tmp);
}
