def solution(a, b):
    days = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    day = 0
    for i in range(1, a):
        day += month[i]
    day += b
    # day 는 1월 1일부터 "n"일째 되는 날..
    return days[day % 7]

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.3MB)
테스트 11 〉	통과 (0.00ms, 10.3MB)
테스트 12 〉	통과 (0.00ms, 10.4MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.4MB)
"""

def solution(a, b):
    days_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    days = sum(days_month[0:a - 1]) + b - 1
    answer = days % 7
    return day_week[answer]
    
"""js
function solution(a, b) {
  const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  const week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];

  const days =
    a > 1 ? month.slice(0, a - 1).reduce((a, b) => a + b) + b - 1 : b - 1;
  const answer = days % 7;
  return week[answer];
}
"""