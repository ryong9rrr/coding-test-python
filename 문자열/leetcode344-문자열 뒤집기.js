// 투포인터 / 106ms
var reverseString = function (s) {
  let left = 0
  let right = s.length - 1

  while (left < right) {
    let temp = s[left]
    s[left] = s[right]
    s[right] = temp
    left++
    right--
  }
}

// 배열 메서드 reverse() 사용 // 100ms
var reverseString = function (s) {
  s.reverse()
}
