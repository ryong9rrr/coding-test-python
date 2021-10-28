def solution(s):
    return "".join(sorted(s, reverse=True))

"""js
function solution(s) {
  return s.split("").sort().reverse().join("");
}
"""
