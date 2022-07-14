def solution(genres, plays):
    table = {}

    for i, genre in enumerate(genres):
        play = plays[i]
        if not genre in table:
            table[genre] = {
                'total': 0,
                'items': []
            }
        table[genre]['total'] += play
        table[genre]['items'].append([i, play])

    for genre in table:
        table[genre]['items'].sort(key = lambda x: x[1], reverse = True)
        table[genre]['items'] = table[genre]['items'][0:2]

    sorted_genres = sorted(
                    [[key, value['total']] for key, value in table.items()],
                    key = lambda x: x[1],
                    reverse = True)

    result = []

    for genre, total in sorted_genres:
        values = [x[0] for x in table[genre]['items']]
        result += values

    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.05ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.06ms, 10.4MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.05ms, 10.2MB)
테스트 14 〉	통과 (0.09ms, 10.4MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
"""