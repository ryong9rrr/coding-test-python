def solution(a, b):
    days_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    days = sum(days_month[0:a-1])
    answer = (days + b - 1) % 7
    return day_week[answer]

"""js
function solution(a, b) {
  const daysOfMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  const dayOfWeek = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];

  const temp = daysOfMonth.slice(0, a - 1);

  let days = 0;
  for (var i = 0; i < temp.length; i++) {
    days += temp[i];
  }
  var answer = (days + b - 1) % 7;

  return dayOfWeek[answer];
}
"""