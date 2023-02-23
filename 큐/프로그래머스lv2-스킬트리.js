function checkSkill(skill, skillTrees) {
  skill.reverse()
  skillTrees.reverse()
  while (skill.length > 0 && skillTrees.length > 0) {
    if (skill.pop() !== skillTrees.pop()) return 0
  }
  return 1
}

function solution(skill, skill_trees) {
  const dict = {}
  for (let i = 0; i < skill.length; i++) {
    dict[skill[i]] = i + 1
  }

  let result = 0

  for (const skillTree of skill_trees) {
    let shortSkill = []
    for (const char of skillTree) {
      if (dict[char]) shortSkill.push(char)
    }
    result += checkSkill([...skill], shortSkill)
  }
  return result
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.14ms, 30.1MB)
// 테스트 2 〉	통과 (0.14ms, 29.9MB)
// 테스트 3 〉	통과 (0.20ms, 30.2MB)
// 테스트 4 〉	통과 (0.17ms, 30.1MB)
// 테스트 5 〉	통과 (0.15ms, 30.2MB)
// 테스트 6 〉	통과 (0.14ms, 30MB)
// 테스트 7 〉	통과 (0.42ms, 29.9MB)
// 테스트 8 〉	통과 (0.16ms, 30.1MB)
// 테스트 9 〉	통과 (0.34ms, 30.1MB)
// 테스트 10 〉	통과 (0.14ms, 30.2MB)
// 테스트 11 〉	통과 (0.43ms, 30.1MB)
// 테스트 12 〉	통과 (0.46ms, 30MB)
// 테스트 13 〉	통과 (0.16ms, 30.2MB)
// 테스트 14 〉	통과 (0.14ms, 30.2MB)
