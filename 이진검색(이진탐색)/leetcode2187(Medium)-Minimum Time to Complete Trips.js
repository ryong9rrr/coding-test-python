// 파라메트릭 서치 : 327ms(24.66%), 58.1MB(16.44%)
/**
 * @param {number[]} time
 * @param {number} totalTrips
 * @return {number}
 */
var minimumTime = function (time, totalTrips) {
  time = time.sort((a, b) => a - b)

  let left = time[0]
  let right = time[time.length - 1] * totalTrips

  const isEnough = (mid) => {
    let acc = 0
    for (const t of time) {
      acc += Math.floor(mid / t)
      if (acc >= totalTrips) {
        return true
      }
    }
    return false
  }

  while (left < right) {
    const mid = Math.floor(left / 2 + right / 2)
    if (isEnough(mid)) {
      right = mid
    } else {
      left = mid + 1
    }
  }

  return left
}
