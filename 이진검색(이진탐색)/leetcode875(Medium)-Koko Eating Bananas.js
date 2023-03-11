// 이분탐색(파라메트릭 서치) 풀이
// - 시간복잡도 : piles의 가장 큰 수를 N이라 할 때 O(logN)
// - 공간복잡도 : O(1)
/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function (piles, h) {
  let left = 1
  let right = Math.max(...piles)

  const isSlow = (mid) => {
    let acc = 0
    for (const pile of piles) {
      acc += Math.ceil(pile / mid)
      if (acc > h) {
        return true
      }
    }
    return false
  }

  while (left < right) {
    const mid = left + Math.floor((right - left) / 2)
    if (isSlow(mid)) {
      left = mid + 1
    } else {
      right = mid
    }
  }

  return left
}
