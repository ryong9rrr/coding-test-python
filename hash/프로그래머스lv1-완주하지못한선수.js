// completion 기준으로 dictionary를 만든다.

function solution(participant, completion) {
  let obj = {};
  completion.forEach((v, i) => {
    if (obj[v]) obj[v]++;
    else obj[v] = 1;
  });
  // 여기서 forEach를 쓰면 안된다. forEach는 undefined를 리턴하기 때문에
  // const result = map... 도 좋지 않다. 모든 구간에서 return 하지 않은 값들에 대해 undefined를 리턴하기 때문에 [undefined, undefined, undefined ... 정답, undefined ...] 형태가 되버림
  for (let i = 0; i < participant.length; i++) {
    const x = participant[i];
    if (!obj[x]) return x;
    obj[x]--;
  }
}

/*
정확성  테스트
테스트 1 〉	통과 (0.23ms, 30.4MB)
테스트 2 〉	통과 (0.23ms, 30.3MB)
테스트 3 〉	통과 (0.29ms, 30.3MB)
테스트 4 〉	통과 (0.32ms, 30.5MB)
테스트 5 〉	통과 (0.40ms, 30.3MB)
효율성  테스트
테스트 1 〉	통과 (16.40ms, 46.9MB)
테스트 2 〉	통과 (19.73ms, 51.1MB)
테스트 3 〉	통과 (21.42ms, 54.9MB)
테스트 4 〉	통과 (28.08ms, 62.4MB)
테스트 5 〉	통과 (33.24ms, 62.6MB)
*/

// 단순 sorting
function solution(participant, completion) {
  let par = participant.sort();
  let com = completion.sort();
  let i = 0;
  while (true) {
    i++;
    if (par[i] !== com[i]) {
      break;
    }
  }
  return par[i];
}
/*
정확성  테스트
테스트 1 〉	통과 (0.07ms, 30MB)
테스트 2 〉	통과 (0.07ms, 30.1MB)
테스트 3 〉	통과 (0.45ms, 30.2MB)
테스트 4 〉	통과 (0.80ms, 30.3MB)
테스트 5 〉	통과 (0.59ms, 30.1MB)
효율성  테스트
테스트 1 〉	통과 (43.82ms, 41.2MB)
테스트 2 〉	통과 (75.16ms, 47.8MB)
테스트 3 〉	통과 (95.45ms, 52.7MB)
테스트 4 〉	통과 (105.75ms, 55.3MB)
테스트 5 〉	통과 (104.44ms, 53.8MB)
*/
