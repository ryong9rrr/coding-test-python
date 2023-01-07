/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length === 1) {
    return nums[0];
  }

  const dp = [nums[0], Math.max(nums[0], nums[1])];
  for (let i = 2; i < nums.length; i += 1) {
    const value = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
    dp.push(value);
  }
  return dp[dp.length - 1];
};
