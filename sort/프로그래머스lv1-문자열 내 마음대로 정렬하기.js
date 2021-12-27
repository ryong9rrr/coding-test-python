function solution(strings, n) {
  const compare = (a, b) => {
    if (a[n] == b[n]) {
      return (a > b) - (a < b);
    } else {
      return (a[n] > b[n]) - (a[n] < b[n]);
    }
  };

  return strings.sort(compare);
}
/*
정확성  테스트
테스트 1 〉	통과 (0.10ms, 30.2MB)
테스트 2 〉	통과 (0.06ms, 30MB)
테스트 3 〉	통과 (0.10ms, 30.4MB)
테스트 4 〉	통과 (0.08ms, 30.4MB)
테스트 5 〉	통과 (0.06ms, 30.3MB)
테스트 6 〉	통과 (0.08ms, 30.1MB)
테스트 7 〉	통과 (0.06ms, 30.4MB)
테스트 8 〉	통과 (0.10ms, 30.3MB)
테스트 9 〉	통과 (0.06ms, 30.3MB)
테스트 10 〉	통과 (0.09ms, 30.3MB)
테스트 11 〉	통과 (0.06ms, 30.3MB)
테스트 12 〉	통과 (0.10ms, 30.2MB)
*/

/*
python

def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x))
*/
