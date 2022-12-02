class LRU {
  HIT = 1;
  MISS = 5;

  constructor(maxSize) {
    this.maxSize = maxSize;
    this.array = [];
    this.time = 0;
  }

  findIndex(value) {
    return this.array.findIndex((item) => item === value);
  }

  remove(valueIndex) {
    this.array.splice(valueIndex, 1);
  }

  isMaxSize() {
    return this.array.length === this.maxSize;
  }

  add(value) {
    const existingIndex = this.findIndex(value);
    if (existingIndex > -1) {
      this.remove(existingIndex);
      this.time += this.HIT;
    } else {
      this.time += this.MISS;
    }
    if (this.isMaxSize()) {
      this.array.shift();
    }
    this.array.push(value);
  }
}

function solution(cacheSize, cities) {
  if (cacheSize === 0) {
    return cities.length * 5;
  }

  const pageChangeAlgorithm = new LRU(cacheSize);

  for (const city of cities) {
    pageChangeAlgorithm.add(city.toLowerCase());
  }

  return pageChangeAlgorithm.time;
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.20ms, 33.4MB)
// 테스트 2 〉	통과 (0.21ms, 33.4MB)
// 테스트 3 〉	통과 (0.21ms, 33.4MB)
// 테스트 4 〉	통과 (0.22ms, 33.5MB)
// 테스트 5 〉	통과 (0.13ms, 33.4MB)
// 테스트 6 〉	통과 (0.04ms, 33.2MB)
// 테스트 7 〉	통과 (0.04ms, 33.1MB)
// 테스트 8 〉	통과 (0.23ms, 33.5MB)
// 테스트 9 〉	통과 (0.21ms, 33.2MB)
// 테스트 10 〉	통과 (0.29ms, 33.4MB)
// 테스트 11 〉	통과 (42.86ms, 41.5MB)
// 테스트 12 〉	통과 (0.31ms, 33.2MB)
// 테스트 13 〉	통과 (0.34ms, 33.4MB)
// 테스트 14 〉	통과 (0.37ms, 33.4MB)
// 테스트 15 〉	통과 (0.42ms, 33.5MB)
// 테스트 16 〉	통과 (0.50ms, 33.7MB)
// 테스트 17 〉	통과 (0.04ms, 33.5MB)
// 테스트 18 〉	통과 (0.94ms, 33.7MB)
// 테스트 19 〉	통과 (1.11ms, 33.7MB)
// 테스트 20 〉	통과 (2.52ms, 33.7MB)
