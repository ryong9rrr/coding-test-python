// completion 기준으로 dictionary를 만든다.

function solution(participant, completion) {
  let com = {};

  for (let i = 0; i < completion.length; i++) {
    const x = completion[i];
    if (com[x]) com[x]++;
    else com[x] = 1;
  }

  for (let i = 0; i < participant.length; i++) {
    const x = participant[i];
    if (!com[x]) return x;
    com[x]--;
  }
}

/*
정확성  테스트
테스트 1 〉	통과 (0.24ms, 30.2MB)
테스트 2 〉	통과 (0.07ms, 30MB)
테스트 3 〉	통과 (0.20ms, 30.3MB)
테스트 4 〉	통과 (0.63ms, 30.4MB)
테스트 5 〉	통과 (0.25ms, 30.4MB)
효율성  테스트
테스트 1 〉	통과 (58.56ms, 46.5MB)
테스트 2 〉	통과 (42.74ms, 51.3MB)
테스트 3 〉	통과 (40.05ms, 54.2MB)
테스트 4 〉	통과 (31.22ms, 62.2MB)
테스트 5 〉	통과 (70.06ms, 62.1MB)
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
