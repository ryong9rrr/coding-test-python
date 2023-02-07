// 해시 방식의 슬라이딩 윈도우 : O(N), 460ms(21.26%), 57.8MB(28.68%)
/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function (fruits) {
  let result = 0
  let left = 0
  const baskets = {}

  for (let right = 0; right < fruits.length; right += 1) {
    const fruit = fruits[right]
    baskets[fruit] = (baskets[fruit] || 0) + 1

    while (Object.keys(baskets).length > 2) {
      baskets[fruits[left]] -= 1
      if (baskets[fruits[left]] === 0) {
        delete baskets[fruits[left]]
      }
      left += 1
    }

    result = Math.max(result, right - left + 1)
  }

  return result
}
