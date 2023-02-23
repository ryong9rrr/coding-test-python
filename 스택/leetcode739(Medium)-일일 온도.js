// stack 풀이 : 266ms(95.98%), 64.1MB
/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
  const answer = new Array(temperatures.length).fill(0)

  const stack = []
  temperatures.forEach((cur, i) => {
    while (stack.length > 0 && temperatures[stack[stack.length - 1]] < cur) {
      const last = stack.pop()
      answer[last] = i - last
    }
    stack.push(i)
  })

  return answer
}
