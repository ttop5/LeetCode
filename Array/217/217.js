/**
* @param {number[]} nums
* @return {boolean}
*/
function containsDuplicate(nums) {
  let isRepeat = false;
  if (nums.length > 1) {
    nums.sort();
    for (let i=1; i< nums.length; i++) {
      if (nums[i] === nums[i-1]) {
        isRepeat = true;
      }
    }
  }
  return isRepeat;
}
