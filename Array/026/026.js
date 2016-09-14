/**
 * @param {number[]} nums
 * @return {number}
 */
function removeDuplicates(nums) {
  let len = 1; // 最少有一个元素不重复
  for (let i=1; i<nums.length; i++) { // 从第2个元素开始跟前面一个比较
    if (nums[i] !== nums[i-1]) {
      nums[len++] = nums[i]; // 不等于前一个元素的话长度加1，并将新元素加到前len个
    }
  }
  return len;
}
