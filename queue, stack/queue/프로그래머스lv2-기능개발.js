function solution(progresses, speeds) {
  var answer = [];

  let head = 0;
  let tail = progresses.length;
  let day = 0;
  let count;

  while (head != tail) {
    count = 0;
    day++;
    for (let i = head; i < tail; i++) {
      if (progresses[i] + speeds[i] * day < 100) break;
      count++;
    }
    if (count) {
      answer.push(count);
      head += count;
    }
  }

  return answer;
}

/*
정확성  테스트
테스트 1 〉	통과 (0.11ms, 30.2MB)
테스트 2 〉	통과 (0.12ms, 30.3MB)
테스트 3 〉	통과 (0.07ms, 30.5MB)
테스트 4 〉	통과 (0.07ms, 30.2MB)
테스트 5 〉	통과 (0.07ms, 30.2MB)
테스트 6 〉	통과 (0.14ms, 30.3MB)
테스트 7 〉	통과 (0.07ms, 30.3MB)
테스트 8 〉	통과 (0.06ms, 30MB)
테스트 9 〉	통과 (0.07ms, 30.3MB)
테스트 10 〉	통과 (0.09ms, 30.4MB)
테스트 11 〉	통과 (0.05ms, 30.3MB)
*/
