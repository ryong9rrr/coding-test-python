/*
투 포인터
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
  if (height.length === 0) return 0

  let volume = 0
  let left = 0
  let right = height.length - 1
  let left_max = height[left]
  let right_max = height[right]

  while (left < right) {
    left_max = Math.max(left_max, height[left])
    right_max = Math.max(right_max, height[right])

    if (left_max <= right_max) {
      volume += left_max - height[left]
      left++
    } else {
      volume += right_max - height[right]
      right--
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
      const waters = Math.min(height[i], height[stack[stack.length - 1]]) - height[top]
      volume += distance * waters
    }
    stack.push(i)
  }

  return volume
}
