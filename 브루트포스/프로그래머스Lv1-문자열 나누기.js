function solution(s) {
  let result = 0;
  let cnt1 = 0;
  let cnt2 = 0;
  let fixture = "";

  for (const char of s) {
    if (!fixture) {
      fixture = char;
    }

    if (fixture === char) {
      cnt1 += 1;
    } else {
      cnt2 += 1;
    }

    if (cnt1 === cnt2) {
      result += 1;
      cnt1 = cnt2 = 0;
      fixture = "";
    }
  }

  if (fixture) {
    result += 1;
  }

  return result;
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.06ms, 33.4MB)
// 테스트 2 〉	통과 (0.42ms, 33.7MB)
// 테스트 3 〉	통과 (0.70ms, 33.9MB)
// 테스트 4 〉	통과 (0.07ms, 33.4MB)
// 테스트 5 〉	통과 (0.05ms, 33.4MB)
// 테스트 6 〉	통과 (0.05ms, 33.4MB)
// 테스트 7 〉	통과 (0.07ms, 33.5MB)
// 테스트 8 〉	통과 (0.05ms, 33.5MB)
// 테스트 9 〉	통과 (0.54ms, 33.6MB)
// 테스트 10 〉	통과 (0.55ms, 33.8MB)
// 테스트 11 〉	통과 (0.40ms, 33.6MB)
// 테스트 12 〉	통과 (0.77ms, 33.6MB)
// 테스트 13 〉	통과 (4.79ms, 37.2MB)
// 테스트 14 〉	통과 (3.36ms, 37.1MB)
// 테스트 15 〉	통과 (0.26ms, 33.6MB)
// 테스트 16 〉	통과 (4.26ms, 36.9MB)
// 테스트 17 〉	통과 (0.42ms, 33.7MB)
// 테스트 18 〉	통과 (0.61ms, 33.7MB)
// 테스트 19 〉	통과 (0.44ms, 33.7MB)
// 테스트 20 〉	통과 (0.75ms, 33.9MB)
// 테스트 21 〉	통과 (3.13ms, 37.1MB)
// 테스트 22 〉	통과 (0.50ms, 33.6MB)
// 테스트 23 〉	통과 (0.32ms, 33.5MB)
// 테스트 24 〉	통과 (0.39ms, 33.7MB)
// 테스트 25 〉	통과 (3.53ms, 37.2MB)
// 테스트 26 〉	통과 (1.05ms, 33.8MB)
// 테스트 27 〉	통과 (0.95ms, 33.8MB)
// 테스트 28 〉	통과 (0.42ms, 33.6MB)
// 테스트 29 〉	통과 (4.75ms, 37.1MB)
// 테스트 30 〉	통과 (0.74ms, 33.7MB)
// 테스트 31 〉	통과 (0.05ms, 33.4MB)
// 테스트 32 〉	통과 (0.05ms, 33.4MB)
// 테스트 33 〉	통과 (0.05ms, 33.5MB)
// 테스트 34 〉	통과 (0.05ms, 33.5MB)
// 테스트 35 〉	통과 (0.07ms, 33.4MB)
// 테스트 36 〉	통과 (0.05ms, 33.6MB)
// 테스트 37 〉	통과 (0.05ms, 33.5MB)
// 테스트 38 〉	통과 (0.05ms, 33.6MB)
// 테스트 39 〉	통과 (0.05ms, 33.6MB)
// 테스트 40 〉	통과 (0.23ms, 33.4MB)
// 테스트 41 〉	통과 (3.19ms, 37.1MB)
// 테스트 42 〉	통과 (3.19ms, 37.2MB)
