// 정규표현식
function solution(str1, str2) {
  const reg = new RegExp(str2, 'g')
  return reg.test(str1) ? 1 : 2
}

// includes
function solution(str1, str2) {
  return str1.includes(str2) ? 1 : 2
}

// indexOf
function solution(str1, str2) {
  return str1.indexOf(str2) > -1 ? 1 : 2
}
