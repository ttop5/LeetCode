/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
function sortColors(nums) {
  let [i, start, end] = [0, 0, nums.length-1];
  while(i <= end) {
    if(nums[i] === 0){
      [nums[i], nums[start]] = [nums[start], nums[i]];
      start += 1;
      i += 1;
    } else if(nums[i] === 2) {
      [nums[i], nums[end]] = [nums[end], nums[i]];
      end -= 1;
    } else {
      i += 1;
    }
  }
}
