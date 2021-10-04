function solution(s) {
  s = s.toUpperCase();

  if (s.split("P").length != s.split("Y").length) return false;
  else return true;
}

function solution(s) {
  if (s.match(/p/gi).length !== s.match(/y/gi).length) return false;
  else return true;
}

/* python

#python
def solution(s):
    s = s.upper()

    if s.count("P") != s.count("Y"):
        return False

    return True

*/
