// 824ms(12.50%), 61MB(12.50%)
var SummaryRanges = function () {
  this.arr = new Set()
}

/**
 * @param {number} value
 * @return {void}
 */
SummaryRanges.prototype.addNum = function (value) {
  this.arr.add(value)
}

/**
 * @return {number[][]}
 */
SummaryRanges.prototype.getIntervals = function () {
  const intervals = []
  let left, right
  left = right = -1
  for (const value of Array.from(this.arr).sort((a, b) => a - b)) {
    if (left < 0) {
      left = right = value
    } else if (right + 1 === value) {
      right += 1
    } else {
      intervals.push([left, right])
      left = right = value
    }
  }
  intervals.push([left, right])
  return intervals
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * var obj = new SummaryRanges()
 * obj.addNum(value)
 * var param_2 = obj.getIntervals()
 */
