/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
function intersection(nums1, nums2) {
  const hash = {};

  nums1.forEach(function(item) {
    hash[item] = 1;
  })
  nums2.forEach(function(item){
    if (hash[item]) {
      hash[item] = 2;
    }
  })

  const ans = [];
  for (let k in hash) {
    hash[k] === 2 && (ans.push(+k));
  }

  return ans;
}
