// 3트
const judgeValue = (index, n) => {
  const [a, b] = [Math.floor(index / n), index % n];
  return a < b ? b + 1 : a + 1;
};

function solution(n, left, right) {
  const length = right - left + 1;
  const slicedIndexArr = Array.from({ length }, (v, i) => i + left);
  return slicedIndexArr.map((index) => judgeValue(index, n));
}
// 정확성  테스트
// 테스트 1 〉	통과 (17.14ms, 44.3MB)
// 테스트 2 〉	통과 (12.32ms, 48.9MB)
// 테스트 3 〉	통과 (12.81ms, 48.8MB)
// 테스트 4 〉	통과 (0.32ms, 33.6MB)
// 테스트 5 〉	통과 (0.23ms, 33.4MB)
// 테스트 6 〉	통과 (15.39ms, 43MB)
// 테스트 7 〉	통과 (16.22ms, 42.9MB)
// 테스트 8 〉	통과 (12.22ms, 44.1MB)
// 테스트 9 〉	통과 (14.15ms, 45.2MB)
// 테스트 10 〉	통과 (21.22ms, 44.1MB)
// 테스트 11 〉	통과 (13.67ms, 45.1MB)
// 테스트 12 〉	통과 (15.73ms, 48.8MB)
// 테스트 13 〉	통과 (16.52ms, 47.9MB)
// 테스트 14 〉	통과 (21.57ms, 48.3MB)
// 테스트 15 〉	통과 (18.36ms, 49.9MB)
// 테스트 16 〉	통과 (18.83ms, 50.9MB)
// 테스트 17 〉	통과 (14.22ms, 47.5MB)
// 테스트 18 〉	통과 (15.52ms, 52.1MB)
// 테스트 19 〉	통과 (25.83ms, 49.7MB)
// 테스트 20 〉	통과 (19.71ms, 44.8MB)

// 1트
function makeMatrix(n) {
  const matrix = Array.from({ length: n }, () => new Array(n));
  for (let i = 0; i < n; i++) {
    let x = i;
    let y = i;
    matrix[x][y] = i + 1;
    while (x >= 0) {
      matrix[x][y] = i + 1;
      x--;
    }
    x = i;
    while (y >= 0) {
      matrix[x][y] = i + 1;
      y--;
    }
  }
  return matrix;
}

function solution(n, left, right) {
  return makeMatrix(n)
    .flat()
    .slice(left, right + 1);
}

// 정확성  테스트
// 테스트 1 〉	통과 (47.36ms, 45.6MB)
// 테스트 2 〉	실패 (signal: aborted (core dumped))
// 테스트 3 〉	실패 (signal: aborted (core dumped))
// 테스트 4 〉	통과 (1.65ms, 33.5MB)
// 테스트 5 〉	통과 (1.79ms, 33.7MB)
// 테스트 6 〉	통과 (179.81ms, 74MB)
// 테스트 7 〉	통과 (238.15ms, 79.1MB)
// 테스트 8 〉	통과 (160.61ms, 74.8MB)
// 테스트 9 〉	실패 (signal: aborted (core dumped))
// 테스트 10 〉	실패 (signal: aborted (core dumped))
// 테스트 11 〉	실패 (signal: aborted (core dumped))
// 테스트 12 〉	실패 (signal: aborted (core dumped))
// 테스트 13 〉	실패 (signal: aborted (core dumped))
// 테스트 14 〉	실패 (signal: aborted (core dumped))
// 테스트 15 〉	실패 (signal: aborted (core dumped))
// 테스트 16 〉	실패 (signal: aborted (core dumped))
// 테스트 17 〉	실패 (signal: aborted (core dumped))
// 테스트 18 〉	실패 (signal: aborted (core dumped))
// 테스트 19 〉	실패 (signal: aborted (core dumped))
// 테스트 20 〉	실패 (signal: aborted (core dumped))

// 2트
function makeMatrix(n) {
  const matrix = Array.from({ length: n }, () => new Array(n));
  for (let i = 0; i < n; i++) {
    let x = i;
    let y = i;
    matrix[x][y] = i + 1;
    while (x >= 0) {
      matrix[x][y] = i + 1;
      x--;
    }
    x = i;
    while (y >= 0) {
      matrix[x][y] = i + 1;
      y--;
    }
  }
  return matrix;
}

const divide = (a, b) => {
  return [Math.floor(a / b), a % b];
};

function solution(n, left, right) {
  const matrix = makeMatrix(n);
  const length = right - left + 1;
  const points = Array.from({ length }, (v, i) => i + left)
    .map((index) => divide(index, n))
    .map(([x, y]) => matrix[x][y]);

  return points;
}
// 정확성  테스트
// 테스트 1 〉	통과 (32.27ms, 58.6MB)
// 테스트 2 〉	실패 (signal: aborted (core dumped))
// 테스트 3 〉	실패 (signal: aborted (core dumped))
// 테스트 4 〉	통과 (0.59ms, 33.6MB)
// 테스트 5 〉	통과 (0.55ms, 33.5MB)
// 테스트 6 〉	통과 (36.00ms, 62.4MB)
// 테스트 7 〉	통과 (32.13ms, 61.7MB)
// 테스트 8 〉	통과 (30.79ms, 61.4MB)
// 테스트 9 〉	통과 (3302.02ms, 797MB)
// 테스트 10 〉	통과 (3369.03ms, 829MB)
// 테스트 11 〉	통과 (2287.00ms, 612MB)
// 테스트 12 〉	실패 (signal: aborted (core dumped))
// 테스트 13 〉	실패 (signal: aborted (core dumped))
// 테스트 14 〉	실패 (signal: aborted (core dumped))
// 테스트 15 〉	실패 (signal: aborted (core dumped))
// 테스트 16 〉	실패 (signal: aborted (core dumped))
// 테스트 17 〉	실패 (signal: aborted (core dumped))
// 테스트 18 〉	실패 (signal: aborted (core dumped))
// 테스트 19 〉	실패 (signal: aborted (core dumped))
// 테스트 20 〉	실패 (signal: aborted (core dumped))
