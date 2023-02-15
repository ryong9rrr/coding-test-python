// num의 길이는 최대 1000
// BigInt 사용하기: 129ms(41.61%), 47.7MB(64.29%)
/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function (num, k) {
  const number = BigInt(num.map((x) => String(x)).join(""))

  return [...String(number + BigInt(k))].map((x) => parseInt(x, 10))
}

// 수학적, 정석적인 방법 : 114ms(65.53%), 46.6MB(89.44%)
/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function (num, k) {
  num[num.length - 1] += k

  for (let i = num.length - 1; i >= 0; i -= 1) {
    k = Math.floor(num[i] / 10)
    num[i] = num[i] % 10

    if (k === 0) {
      break
    }
    if (i > 0) {
      num[i - 1] += k
    }
  }

  if (k > 0) {
    const rest = [...String(k)].map((x) => parseInt(x, 10))
    num = [...rest, ...num]
  }

  return num
}
