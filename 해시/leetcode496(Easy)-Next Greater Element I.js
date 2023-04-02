/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function (nums1, nums2) {
  const indexTable = nums2.reduce((obj, num, index) => {
    obj[num] = index
    return obj
  }, {})

  const search = (targetNumber, startIndex) => {
    for (let i = startIndex; i < nums2.length; i += 1) {
      if (nums2[i] > targetNumber) {
        return nums2[i]
      }
    }
    return -1
  }

  return nums1.map((num) => {
    const index = indexTable[num]
    return search(num, index + 1)
  })
}
