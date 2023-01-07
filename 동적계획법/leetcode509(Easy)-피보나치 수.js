// 일반 재귀 : 153ms, 42.1MB
/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
  if (n <= 1) {
    return n;
  }
  return fib(n - 2) + fib(n - 1);
};

// 메모이제이션 : 119ms, 41.7MB
/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
  const dp = {
    0: 0,
    1: 1,
  };

  function fibonacci(x) {
    if (x in dp) {
      return dp[x];
    }
    dp[x] = fibonacci(x - 2) + fibonacci(x - 1);
    return dp[x];
  }

  return fibonacci(n);
};

// 타뷸레이션 : 130ms, 42.2MB
/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
  const dp = [0, 1];
  for (let i = 2; i < n + 1; i += 1) {
    dp.push(dp[i - 2] + dp[i - 1]);
  }
  return dp[n];
};

// 스왑 방식 : 95ms, 42.4MB
/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
  let x = 0;
  let y = 1;
  for (let i = 0; i < n; i += 1) {
    const temp = x + y;
    x = y;
    y = temp;
  }
  return x;
};
