const translateDate = (date) => {
  const [y, m, d] = date.split(".").map((s) => Number(s))
  const year = (y - 2000) * 28 * 12
  const month = 28 * (m - 1)
  return year + month + d
}

const getExpiredDay = (day, validity) => {
  return day + 28 * validity - 1
}

function solution(today, terms, privacies) {
  const termsMap = terms
    .map((term) => term.split(" "))
    .reduce((obj, [vType, v]) => {
      obj[vType] = Number(v)
      return obj
    }, {})

  return privacies
    .map((privacy) => privacy.split(" "))
    .reduce((result, [date, vType], i) => {
      const expiredDay = getExpiredDay(translateDate(date), termsMap[vType])
      if (expiredDay < translateDate(today)) {
        result.push(i + 1)
      }
      return result
    }, [])
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.17ms, 33.2MB)
// 테스트 2 〉	통과 (0.30ms, 33.4MB)
// 테스트 3 〉	통과 (0.21ms, 33.4MB)
// 테스트 4 〉	통과 (0.20ms, 33.1MB)
// 테스트 5 〉	통과 (0.29ms, 33.5MB)
// 테스트 6 〉	통과 (0.39ms, 33.5MB)
// 테스트 7 〉	통과 (0.37ms, 33.5MB)
// 테스트 8 〉	통과 (0.43ms, 33.4MB)
// 테스트 9 〉	통과 (0.89ms, 33.5MB)
// 테스트 10 〉	통과 (0.50ms, 33.5MB)
// 테스트 11 〉	통과 (0.49ms, 33.6MB)
// 테스트 12 〉	통과 (0.62ms, 33.6MB)
// 테스트 13 〉	통과 (0.63ms, 33.7MB)
// 테스트 14 〉	통과 (0.54ms, 33.5MB)
// 테스트 15 〉	통과 (0.54ms, 33.5MB)
// 테스트 16 〉	통과 (0.74ms, 33.5MB)
// 테스트 17 〉	통과 (0.67ms, 33.6MB)
// 테스트 18 〉	통과 (1.08ms, 33.6MB)
// 테스트 19 〉	통과 (0.68ms, 33.6MB)
// 테스트 20 〉	통과 (0.68ms, 33.6MB)
