const HAMBURGER = "1231";

const hasHamburger = (stack) => {
  return stack.slice(-HAMBURGER.length).join("") === HAMBURGER;
};

const removeHamburger = (stack) => {
  for (let i = 0; i < HAMBURGER.length; i++) {
    stack.pop();
  }
};

function solution(ingredient) {
  let result = 0;
  const stack = [];

  ingredient.forEach((x) => {
    stack.push(x);
    if (hasHamburger(stack)) {
      removeHamburger(stack);
      result += 1;
    }
  });

  return result;
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.08ms, 33.5MB)
// 테스트 2 〉	통과 (0.08ms, 33.5MB)
// 테스트 3 〉	통과 (63.29ms, 59.5MB)
// 테스트 4 〉	통과 (139.06ms, 82.3MB)
// 테스트 5 〉	통과 (204.05ms, 84.5MB)
// 테스트 6 〉	통과 (104.90ms, 68.2MB)
// 테스트 7 〉	통과 (124.50ms, 79.6MB)
// 테스트 8 〉	통과 (110.70ms, 68.4MB)
// 테스트 9 〉	통과 (72.55ms, 63.6MB)
// 테스트 10 〉	통과 (3.18ms, 36.7MB)
// 테스트 11 〉	통과 (73.48ms, 57.2MB)
// 테스트 12 〉	통과 (212.75ms, 98.1MB)
// 테스트 13 〉	통과 (0.06ms, 33.5MB)
// 테스트 14 〉	통과 (0.08ms, 33.5MB)
// 테스트 15 〉	통과 (0.06ms, 33.5MB)
// 테스트 16 〉	통과 (0.06ms, 33.5MB)
// 테스트 17 〉	통과 (0.06ms, 33.5MB)
// 테스트 18 〉	통과 (0.16ms, 33.6MB)
