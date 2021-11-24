def solution(n):
    sosu = [True] * (n+1)
    for num in range(2, int(n**0.5)+1) :
        if sosu[num] :
            for i in range(num*num, n+1, num) :
                sosu[i] = False
    result = [x for x in range(2,n+1) if sosu[x]==True]
    return len(result)

"""js
function solution(n) {
  let sosu = Array.from({ length: n + 1 }, (v) => true);

  for (var num = 2; num <= Math.sqrt(n); num++) {
    if (sosu[num]) {
      for (var i = num * num; i <= n; i += num) {
        sosu[i] = false;
      }
    }
  }
  const result = sosu.filter((x) => x == true);
  return result.length - 2;
}
"""