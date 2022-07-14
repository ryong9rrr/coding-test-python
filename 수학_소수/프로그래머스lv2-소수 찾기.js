function permute(nums, k) {
  if (k > nums.length) return undefined;
  const results = [];
  prevElements = [];
  function dfs(elements, k) {
    if (k === 0) {
      results.push([...prevElements]);
      return;
    }

    for (let i = 0; i < elements.length; i++) {
      nextElements = [...elements];
      nextElements.splice(i, 1);

      prevElements.push(elements[i]);
      dfs(nextElements, k - 1);
      prevElements.pop();
    }
  }
  dfs(nums, k);
  return results;
}

function makePrimeNumbers(n) {
  const primeNumbers = Array.from({ length: n + 1 }, (v) => true);
  primeNumbers.splice(0, 2, false, false);
  for (let num = 2; num < Math.floor(Math.sqrt(n)) + 1; num++) {
    if (primeNumbers[num]) {
      for (let i = num * num; i < n + 1; i += num) {
        primeNumbers[i] = false;
      }
    }
  }
  return primeNumbers;
}

function solution(numbers) {
  const n = Number(Array.from(numbers).sort().reverse().join(""));
  const primeNumbers = makePrimeNumbers(n);
  const permutations = new Set([]);
  for (let k = 1; k <= numbers.length; k++) {
    const permutation = permute(numbers, k);
    for (const arr of permutation) {
      permutations.add(Number(arr.join("")));
    }
  }

  let count = 0;
  for (const num of [...permutations]) {
    if (primeNumbers[num]) count++;
  }
  return count;
}

/*
정확성  테스트
테스트 1 〉	통과 (0.98ms, 30MB)
테스트 2 〉	통과 (91.36ms, 37.6MB)
테스트 3 〉	통과 (0.37ms, 30MB)
테스트 4 〉	통과 (48.10ms, 34.7MB)
테스트 5 〉	통과 (595.38ms, 62.7MB)
테스트 6 〉	통과 (0.38ms, 30MB)
테스트 7 〉	통과 (1.57ms, 30MB)
테스트 8 〉	통과 (1039.83ms, 78.3MB)
테스트 9 〉	통과 (0.51ms, 30.1MB)
테스트 10 〉	통과 (195.11ms, 39.8MB)
테스트 11 〉	통과 (18.39ms, 32.6MB)
테스트 12 〉	통과 (11.94ms, 33MB)
*/
