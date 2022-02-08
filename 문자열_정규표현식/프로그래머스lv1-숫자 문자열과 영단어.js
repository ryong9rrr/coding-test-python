function solution(s) {
  const nums = [
    /zero/g,
    /one/g,
    /two/g,
    /three/g,
    /four/g,
    /five/g,
    /six/g,
    /seven/g,
    /eight/g,
    /nine/g,
  ];

  nums.forEach((v, i) => {
    s = s.replace(v, String(i));
  });

  return Number(s);
}

/*
정확성  테스트
테스트 1 〉	통과 (0.16ms, 30.1MB)
테스트 2 〉	통과 (0.10ms, 30.2MB)
테스트 3 〉	통과 (0.08ms, 30.3MB)
테스트 4 〉	통과 (0.10ms, 30.3MB)
테스트 5 〉	통과 (0.10ms, 30.2MB)
테스트 6 〉	통과 (0.15ms, 30.2MB)
테스트 7 〉	통과 (0.12ms, 30.3MB)
테스트 8 〉	통과 (0.11ms, 30.2MB)
테스트 9 〉	통과 (0.11ms, 30.2MB)
테스트 10 〉	통과 (0.08ms, 30.6MB)
*/
