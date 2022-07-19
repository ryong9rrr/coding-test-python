function isAlpha(string) {
  const reg = /[a-zA-Z]/g
  return string.replace(reg, '') === ''
}

function isDigit(string) {
  for (const char of string) {
    if (char < '0' || char > '9') {
      return false
    }
  }
  return true
}

function isNumber(string) {
  return !Number.isNaN(Number(string))
}

function isAlnum(string) {
  const reg = /[a-zA-Z0-9]/g
  return string.replace(reg, '') === ''
}

const string = '1231a'

console.log(isAlpha(string))
console.log(isDigit(string))
console.log(isAlnum(string))
console.log(isNumber(string))
