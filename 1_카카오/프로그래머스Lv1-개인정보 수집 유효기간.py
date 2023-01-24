def translate_date(date):
    y, m, d = list(map(int, date.split(".")))
    year = (y - 2000) * 28 * 12
    month = 28 * (m - 1)
    return year + month + d


def get_expired_day(day, validity):
    return (day + 28 * validity) - 1


def solution(today, terms, privacies):
    terms_map = {}
    for validity_type, validity in [x.split(" ") for x in terms]:
        terms_map[validity_type] = int(validity)
        
    result = []
    t_today = translate_date(today)
    for i, v in enumerate([x.split(" ") for x in privacies]):
        date, validity_type = v
        expired_day = get_expired_day(translate_date(date), terms_map[validity_type])
        if expired_day < t_today:
            result.append(i + 1)
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.05ms, 10.3MB)
테스트 6 〉	통과 (0.06ms, 10.4MB)
테스트 7 〉	통과 (0.04ms, 10.4MB)
테스트 8 〉	통과 (0.05ms, 10.4MB)
테스트 9 〉	통과 (0.09ms, 10.4MB)
테스트 10 〉	통과 (0.09ms, 10.4MB)
테스트 11 〉	통과 (0.09ms, 10.4MB)
테스트 12 〉	통과 (0.16ms, 10.3MB)
테스트 13 〉	통과 (0.15ms, 10.4MB)
테스트 14 〉	통과 (0.10ms, 10.4MB)
테스트 15 〉	통과 (0.10ms, 10.4MB)
테스트 16 〉	통과 (0.15ms, 10.5MB)
테스트 17 〉	통과 (0.15ms, 10.4MB)
테스트 18 〉	통과 (0.15ms, 10.4MB)
테스트 19 〉	통과 (0.16ms, 10.5MB)
테스트 20 〉	통과 (0.16ms, 10.4MB)
"""