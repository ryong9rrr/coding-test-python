function subsets(array) {
  const result = [];

  function dfs(index, path) {
    result.push(path);

    for (let i = index; i < array.length; i++) {
      dfs(i + 1, [...path, array[i]]);
    }
    return;
  }

  dfs(0, []);

  return result;
}

const nums = [1, 2, 3];

console.log(subsets(nums)); // [ [], [ 1 ], [ 1, 2 ], [ 1, 2, 3 ], [ 1, 3 ], [ 2 ], [ 2, 3 ], [ 3 ] ]
