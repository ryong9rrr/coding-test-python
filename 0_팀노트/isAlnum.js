function isAlpha(strings) {
  const reg = new RegExp(/^[a-zA-Z]+$/, 'g');
  return reg.test(strings);
}

function isDigit(string) {
  for (const char of string) {
    if (char < '0' || char > '9') {
      return false;
    }
  }
  return true;
}

function isNumber(string) {
  return !Number.isNaN(Number(string));
}

function isAlnum(string) {
  const reg = /[a-zA-Z0-9]/g;
  return string.replace(reg, '') === '';
}
