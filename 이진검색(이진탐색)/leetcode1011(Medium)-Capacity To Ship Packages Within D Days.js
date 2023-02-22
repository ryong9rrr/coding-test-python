// 96ms(43.24%), 46.5MB(9.19%)
const day = (capacity, weights) => {
  let n = 0
  let load = 0
  for (const weight of weights) {
    if (load + weight > capacity) {
      n++
      load = 0
    }
    load += weight
  }
  if (load > 0) {
    n++
  }
  return n
}

/**
 * @param {number[]} weights
 * @param {number} days
 * @return {number}
 */
var shipWithinDays = function (weights, days) {
  let left = 0
  let right = 0
  for (const weight of weights) {
    left = Math.max(left, weight)
    right += weight
  }

  while (left < right) {
    const mid = left + Math.floor((right - left) / 2)
    const needDay = day(mid, weights)

    if (needDay <= days) {
      right = mid
    } else {
      left = mid + 1
    }
  }

  return left
}

// 약간의 최적화 : 72ms(98.38%), 46MB(12.43%)
const feasible = (capacity, weights, days) => {
  let n = 0
  let load = 0
  for (const weight of weights) {
    if (load + weight > capacity) {
      n++
      load = 0
    }
    load += weight
    if (n > days) {
      return false
    }
  }
  if (load > 0) {
    n++
  }
  return n <= days
}

/**
 * @param {number[]} weights
 * @param {number} days
 * @return {number}
 */
var shipWithinDays = function (weights, days) {
  let left = 0
  let right = 0
  for (const weight of weights) {
    left = Math.max(left, weight)
    right += weight
  }

  while (left < right) {
    const mid = left + Math.floor((right - left) / 2)
    if (feasible(mid, weights, days)) {
      right = mid
    } else {
      left = mid + 1
    }
  }

  return left
}
