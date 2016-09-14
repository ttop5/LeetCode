/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * 遍历数组元素分别与之后面的元素相加，满足条件就返回索引
 */
function twoSum(nums, target) {
  for (let i=0; i<nums.length; i++) {
    for (let j=i + 1; j<nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
}
