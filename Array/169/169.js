/**
 * @param {number[]} nums
 * @return {number}
 */
function majorityElement(nums) {
  let numsDic = {};
  for (let i=0; i<nums.length; i++) {
    if (nums[i] in numsDic) {
      numsDic[nums[i]] += 1;
    } else {
      numsDic[nums[i]] = 1;
    }
    if (numsDic[nums[i]] > nums.length/2) {
      return nums[i];
    }
  }
  return 0;
}
