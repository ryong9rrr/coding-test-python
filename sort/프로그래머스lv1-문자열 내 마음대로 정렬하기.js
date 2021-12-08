function solution(strings, n) {
  const compare = (a, b) => {
    if (a[n] == b[n]) {
      return (a > b) - (a < b);
    } else {
      return (a[n] > b[n]) - (a[n] < b[n]);
    }
  };

  return strings.sort(compare);
}

/*
python

def solution(strings, n):
    return sorted(sorted(strings), key=lambda x : x[n])
*/
