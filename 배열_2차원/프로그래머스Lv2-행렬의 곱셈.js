const multiplyMatrix = (matrix1, matrix2) => {
  const multiply = (arr1, arr2) => {
    return arr1.reduce((total, value, i) => total + value * arr2[i], 0);
  };

  const getColumns = (matrix, j) => {
    return Array.from({ length: matrix.length }, (v, i) => i).map(
      (i) => matrix[i][j],
    );
  };

  const result = [];
  for (let i = 0; i < matrix1.length; i += 1) {
    const row = [];
    for (let j = 0; j < matrix2[0].length; j += 1) {
      row.push(multiply(matrix1[i], getColumns(matrix2, j)));
    }
    result.push(row);
  }

  return result;
};

function solution(arr1, arr2) {
  return multiplyMatrix(arr1, arr2);
}

// 정확성  테스트
// 테스트 1 〉	통과 (24.17ms, 37.7MB)
// 테스트 2 〉	통과 (48.22ms, 37.8MB)
// 테스트 3 〉	통과 (69.84ms, 39.3MB)
// 테스트 4 〉	통과 (21.32ms, 36.8MB)
// 테스트 5 〉	통과 (35.54ms, 38MB)
// 테스트 6 〉	통과 (22.12ms, 39.1MB)
// 테스트 7 〉	통과 (2.04ms, 35.6MB)
// 테스트 8 〉	통과 (0.96ms, 33.7MB)
// 테스트 9 〉	통과 (0.83ms, 33.6MB)
// 테스트 10 〉	통과 (35.58ms, 39.1MB)
// 테스트 11 〉	통과 (5.35ms, 36.3MB)
// 테스트 12 〉	통과 (1.34ms, 34.1MB)
// 테스트 13 〉	통과 (31.53ms, 38MB)
// 테스트 14 〉	통과 (50.63ms, 38MB)
// 테스트 15 〉	통과 (18.54ms, 37.4MB)
// 테스트 16 〉	통과 (42.41ms, 38.2MB)
