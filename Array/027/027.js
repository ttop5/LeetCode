/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 * 使用类似于两个指针的思路
 */
function removeElement (nums, val) {
  let j = 0;
  for (let i=0; i<nums.length; i++) {
    if (nums[i] !== val) {
      nums[j++] = nums[i];
    }
  }
  return j;
}
