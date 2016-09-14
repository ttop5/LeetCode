/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
  const narray = [];
  for (let i=0; i<nums.length; i++) {
    for (let j=i + 1; j<nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        narray.push(i) && narray.push(j);
        return narray;
      }
    }
  }
}
