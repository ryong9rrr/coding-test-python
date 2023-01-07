/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  const result = [nums[0]];

  for (let i = 1; i < nums.length; i += 1) {
    const value = Math.max(0, result[i - 1]) + nums[i];
    result.push(value);
  }

  return Math.max(...result);
};

// 카데인 알고리즘
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let bestSum = -Infinity;
  let currentSum = 0;

  nums.forEach((num) => {
    currentSum = Math.max(num, currentSum + num);
    bestSum = Math.max(currentSum, bestSum);
  });

  return bestSum;
};
