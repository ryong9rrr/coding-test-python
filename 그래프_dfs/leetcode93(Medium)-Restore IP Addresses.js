// 143ms(5%), 44.7MB(18.35%)
/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function (s) {
  if (Number.isNaN(Number(s))) {
    return []
  }

  const result = []

  const validate = (array) => {
    const last = Number(array[array.length - 1])
    if (last < 0 || last > 255 || array.length > 4) {
      return false
    }
    return true
  }

  const dfs = (index, array) => {
    if (!validate(array)) {
      return
    }

    if (index >= s.length) {
      if (
        array.length !== 4 ||
        array.find((item) => item.length > 1 && item[0] === "0")
      ) {
        return
      }
      result.push(array.join("."))
      return
    }

    const case1 = [...array, s[index]]
    const case2 = [...array]
    case2[case2.length - 1] += s[index]

    dfs(index + 1, case1)
    dfs(index + 1, case2)
  }

  dfs(1, [s[0]])

  return result
}

// 더 깔끔한 방법.. : 69ms(68.7%), 43MB(57.28%)
/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function (s) {
  const result = []

  const isValid = (str) => {
    if (!str || Number(str) > 255) {
      return false
    }
    if (str.length > 1 && str[0] === "0") {
      return false
    }
    return true
  }

  const dfs = (str, array) => {
    if (array.length === 3) {
      if (isValid(str)) {
        result.push([...array, str].join("."))
      }
      return
    }

    for (let i = 1; i < 4; i++) {
      const subStr = str.slice(0, i)
      if (isValid(subStr)) {
        dfs(str.slice(i), [...array, subStr])
      }
    }
  }

  dfs(s, [])

  return result
}
