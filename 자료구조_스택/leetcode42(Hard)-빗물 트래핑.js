/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
  let left = 0
  let right = height.length - 1

  let leftMax = height[left]
  let rightMax = height[right]
  let volume = 0

  while (left < right) {
    leftMax = Math.max(leftMax, height[left])
    rightMax = Math.max(rightMax, height[right])

    if (leftMax <= rightMax) {
      volume += leftMax - height[left]
      left += 1
    } else {
      volume += rightMax - height[right]
      right -= 1
    }
  }

  return volume
}

// 스택 풀이
var trap = function (height) {
  const stack = []
  let volume = 0

  for (let i = 0; i < height.length; i++) {
    while (stack.length > 0 && height[i] > height[stack[stack.length - 1]]) {
      const top = stack.pop()

      if (stack.length === 0) break

      const distance = i - stack[stack.length - 1] - 1
      const waters =
        Math.min(height[i], height[stack[stack.length - 1]]) - height[top]
      volume += distance * waters
    }
    stack.push(i)
  }

  return volume
}
