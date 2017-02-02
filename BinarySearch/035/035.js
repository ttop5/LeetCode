/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
function searchInsert(nums, target) {
  let high = nums.length - 1;
  let low = 0;
  while (low <= high) {
    let mid = Math.floor((high + low) / 2);
    if (nums[mid] === target) {
      return mid;
    }
    if (target > nums[mid]) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return low;
}
