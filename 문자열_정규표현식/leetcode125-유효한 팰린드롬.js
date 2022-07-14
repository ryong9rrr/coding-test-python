var isPalindrome = function (s) {
  const regex = /[^a-zA-Z0-9]/g

  s = s.replace(regex, '').toLowerCase()

  // reverse() 메서드는 문자열에 사용할 수 없다.
  return s === [...s].reverse().join('')
}
