// nums: int[] -> int[][]
function combine(nums, k) {
  const results = [];

  function dfs(elements, start, k) {
    if (k === 0) {
      results.push([...elements]);
      return;
    }

    for (let i = start; i < nums.length; i++) {
      elements.push(nums[i]);
      dfs(elements, i + 1, k - 1);
      elements.pop();
    }
  }
  dfs([], 0, k);
  return results;
}

const nums = [1, 2, 3, 4, 5];

const combinations = combine(nums, 2);

console.log(combinations);
/*
  [ [ 1, 2 ],
    [ 1, 3 ],
    [ 1, 4 ],
    [ 1, 5 ],
    [ 2, 3 ],
    [ 2, 4 ],
    [ 2, 5 ],
    [ 3, 4 ],
    [ 3, 5 ],
    [ 4, 5 ] ]
  */
