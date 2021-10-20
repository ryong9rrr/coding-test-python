// [Error]: Maximum call stack size exceeded
// 에러가 남.. 더 좋은 로직을 찾아봐야한다.
function dfs(numbers, target, index, total) {
  if (numbers.length === index) {
    return target === total ? 1 : 0;
  }

  let count = 0;
  count += dfs(numbers, target, index + 1, total + numbers[index]);
  count += dfs(numbers, target, index - 1, total - numbers[index]);

  return count;
}

function solution(numbers, target) {
  return dfs(numbers, target, 0, 0);
}
