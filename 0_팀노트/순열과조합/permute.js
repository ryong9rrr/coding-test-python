// nums: int[], k: int -> int[][]
function permute(array, k) {
  if (k > array.length) return null
  const results = []
  const prevElements = []
  function dfs(elements, k) {
    if (k === 0) {
      results.push([...prevElements])
      return
    }

    for (let i = 0; i < elements.length; i++) {
      const nextElements = [...elements]
      nextElements.splice(i, 1)

      prevElements.push(elements[i])
      dfs(nextElements, k - 1)
      prevElements.pop()
    }
  }
  dfs(array, k)
  return results
}

const nums = [1, 2, 3]

for (let i = 1; i <= 3; i++) {
  console.log(permute(nums, i))
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
