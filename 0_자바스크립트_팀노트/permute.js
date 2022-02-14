// nums: int[], k: int -> int[][]
function permute(nums, k) {
  if (k > nums.length) return undefined;
  const results = [];
  prevElements = [];
  function dfs(elements, k) {
    if (k === 0) {
      results.push([...prevElements]);
      return;
    }

    for (let i = 0; i < elements.length; i++) {
      nextElements = [...elements];
      nextElements.splice(i, 1);

      prevElements.push(elements[i]);
      dfs(nextElements, k - 1);
      prevElements.pop();
    }
  }
  dfs(nums, k);
  return results;
}

const nums = [1, 2, 3];

for (let i = 1; i <= 3; i++) {
  console.log(permute(nums, i));
}

/*
[ [ 1 ], [ 2 ], [ 3 ] ]  

[ [ 1, 2 ], [ 1, 3 ], [ 2, 1 ], [ 2, 3 ], [ 3, 1 ], [ 3, 2 ] ] 

[ [ 1, 2, 3 ],
  [ 1, 3, 2 ],
  [ 2, 1, 3 ],
  [ 2, 3, 1 ],
  [ 3, 1, 2 ],
  [ 3, 2, 1 ] ]
*/
