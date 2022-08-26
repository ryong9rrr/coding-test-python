// nums: int[] -> int[][]
function combine(nums, k) {
  const results = []

  function dfs(elements, start, k) {
    if (k === 0) {
      results.push([...elements])
      return
    }

    for (let i = start; i < nums.length; i++) {
      elements.push(nums[i])
      dfs(elements, i + 1, k - 1)
      elements.pop()
    }
  }
  dfs([], 0, k)
  return results
}

function solution(orders, course) {
  const dic = {}

  const sortedOrders = orders.map((order) => order.split('').sort())

  course.forEach((i) => {
    dic[i] = {}
    for (const order of sortedOrders) {
      const combinations = combine(order, i)
      for (const comb of combinations) {
        const menu = comb.join('')
        if (!dic[i][menu]) {
          dic[i][menu] = 0
        }
        dic[i][menu]++
      }
    }
  })

  const result = []
  for (const course in dic) {
    let max = 2
    for (const [key, value] of Object.entries(dic[course])) {
      if (value > max) {
        max = value
      }
    }
    for (const [key, value] of Object.entries(dic[course])) {
      if (value === max) result.push(key)
    }
  }

  return result.sort()
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.79ms, 30.1MB)
// 테스트 2 〉	통과 (0.64ms, 30.3MB)
// 테스트 3 〉	통과 (0.76ms, 30MB)
// 테스트 4 〉	통과 (0.84ms, 30.2MB)
// 테스트 5 〉	통과 (0.83ms, 30MB)
// 테스트 6 〉	통과 (1.27ms, 30.1MB)
// 테스트 7 〉	통과 (1.26ms, 30.2MB)
// 테스트 8 〉	통과 (7.79ms, 33.9MB)
// 테스트 9 〉	통과 (8.08ms, 33.8MB)
// 테스트 10 〉	통과 (11.08ms, 34.8MB)
// 테스트 11 〉	통과 (5.81ms, 33.8MB)
// 테스트 12 〉	통과 (7.65ms, 34.2MB)
// 테스트 13 〉	통과 (10.78ms, 34.2MB)
// 테스트 14 〉	통과 (9.98ms, 34.1MB)
// 테스트 15 〉	통과 (8.84ms, 34.7MB)
// 테스트 16 〉	통과 (4.22ms, 33.1MB)
// 테스트 17 〉	통과 (12.23ms, 33.2MB)
// 테스트 18 〉	통과 (5.93ms, 33.2MB)
// 테스트 19 〉	통과 (3.03ms, 32.6MB)
// 테스트 20 〉	통과 (6.36ms, 33.1MB)

// 22년 8월 풀이
function combine(array, k) {
  const results = []

  function dfs(elements, start, k) {
    if (k === 0) {
      results.push([...elements])
      return
    }

    for (let i = start; i < array.length; i++) {
      elements.push(array[i])
      dfs(elements, i + 1, k - 1)
      elements.pop()
    }
  }
  dfs([], 0, k)
  return results
}

function solution(orders, course) {
  const table = {}
  // 모든 조합의 수로 table 초기화
  for (const i of course) {
    for (const order of orders) {
      const combs = combine(order, i)
      for (const comb of combs) {
        const key = comb.sort().join('')
        if (!table[key]) {
          table[key] = 0
        }
        table[key]++
      }
    }
  }

  // 코스의 길이별로 새로운 table 초기화
  const coursesTable = Object.entries(table).reduce((obj, [key, value]) => {
    if (value !== 1) {
      if (!obj[key.length]) {
        obj[key.length] = []
      }
      obj[key.length].push([key, value])
    }
    return obj
  }, {})

  const result = []

  for (const i in coursesTable) {
    const maxValue = coursesTable[i].sort((a, b) => b[1] - a[1])[0][1]
    const items = coursesTable[i]
      .filter(([key, value]) => value === maxValue)
      .map(([key, value]) => key)

    items.forEach((item) => result.push(item))
  }

  return result.sort()
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.77ms, 30.2MB)
// 테스트 2 〉	통과 (0.74ms, 30.1MB)
// 테스트 3 〉	통과 (0.87ms, 30.2MB)
// 테스트 4 〉	통과 (0.87ms, 30.3MB)
// 테스트 5 〉	통과 (0.79ms, 30.1MB)
// 테스트 6 〉	통과 (1.40ms, 30.2MB)
// 테스트 7 〉	통과 (1.66ms, 30.1MB)
// 테스트 8 〉	통과 (14.10ms, 35MB)
// 테스트 9 〉	통과 (8.63ms, 35MB)
// 테스트 10 〉	통과 (9.80ms, 35.4MB)
// 테스트 11 〉	통과 (9.34ms, 34.1MB)
// 테스트 12 〉	통과 (9.38ms, 34.7MB)
// 테스트 13 〉	통과 (9.09ms, 35.2MB)
// 테스트 14 〉	통과 (7.29ms, 34.5MB)
// 테스트 15 〉	통과 (9.32ms, 34.9MB)
// 테스트 16 〉	통과 (4.00ms, 33.4MB)
// 테스트 17 〉	통과 (5.57ms, 32.8MB)
// 테스트 18 〉	통과 (6.78ms, 33.1MB)
// 테스트 19 〉	통과 (3.25ms, 32.8MB)
// 테스트 20 〉	통과 (10.90ms, 33.2MB)
