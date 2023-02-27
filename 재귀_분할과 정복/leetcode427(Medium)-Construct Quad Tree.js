// 58ms(100%), 47.5MB(36.36%)

// Definition for a QuadTree node.
function Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight) {
  this.val = val
  this.isLeaf = isLeaf
  this.topLeft = topLeft
  this.topRight = topRight
  this.bottomLeft = bottomLeft
  this.bottomRight = bottomRight
}

const divide = (n, i, j, grid) => {
  if (n <= 1) {
    return new Node(grid[i][j], true, null, null, null, null)
  }

  const mid = Math.floor(n / 2)
  const topLeft = divide(mid, i, j, grid)
  const topRight = divide(mid, i, j + mid, grid)
  const bottomLeft = divide(mid, i + mid, j, grid)
  const bottomRight = divide(mid, i + mid, j + mid, grid)

  if (
    topLeft.isLeaf &&
    topRight.isLeaf &&
    bottomLeft.isLeaf &&
    bottomRight.isLeaf &&
    topLeft.val === topRight.val &&
    topRight.val === bottomLeft.val &&
    bottomLeft.val === bottomRight.val
  ) {
    return new Node(topLeft.val, true, null, null, null, null)
  }

  // val (첫번째 인자) 는 아무값이나 넣어도 상관없음.
  return new Node(grid[i][j], false, topLeft, topRight, bottomLeft, bottomRight)
}

/**
 * @param {number[][]} grid
 * @return {Node}
 */
var construct = function (grid) {
  return divide(grid.length, 0, 0, grid)
}
