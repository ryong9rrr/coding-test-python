// 그리디 + 투포인터, 프로그래머스Lv2-구명보트 문제와 동일한 문제
/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function (people, limit) {
  people = people.sort((a, b) => a - b)
  let left = 0
  let right = people.length - 1
  let count = 0

  while (left <= right) {
    if (people[left] + people[right] <= limit) {
      left++
    }
    right--
    count++
  }
  return count
}
