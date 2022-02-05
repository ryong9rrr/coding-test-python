// nums: int[] -> int[][]
function permute(nums) {
  const results = [];
  prevElements = [];
  function dfs(elements) {
    if (elements.length === 0) {
      results.push([...prevElements]);
    }

    for (let i = 0; i < elements.length; i++) {
      nextElements = [...elements];
      nextElements.splice(i, 1);

      prevElements.push(elements[i]);
      dfs(nextElements);
      prevElements.pop();
    }
  }
  dfs(nums);
  return results;
}

const nums = [1, 2, 3];

const permutations = permute(nums);

console.log(permutations);
/*
[ [ 1, 2, 3 ],
  [ 1, 3, 2 ],
  [ 2, 1, 3 ],
  [ 2, 3, 1 ],
  [ 3, 1, 2 ],
  [ 3, 2, 1 ] ]
*/
