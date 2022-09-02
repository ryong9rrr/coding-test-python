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

# 22년 9월 풀이
from collections import defaultdict
def solution(genres, plays):
    N = len(genres)
    songs = defaultdict(list)
    for i, x in enumerate(zip(genres, plays)):
        genre, play = x
        songs[genre].append([i, play])

    # 1. 가장 많이 재생된 순으로 장르배열을 구한다. => <Array>["장르", "재생 수"]
    most_genres = []
    for genre in songs.keys():
        total = sum([x[1] for x in songs[genre]])
        most_genres.append([genre, total])
    most_genres.sort(key = lambda x: x[1], reverse = True)

    # 1에서 구한 배열을 바탕으로 가장 많이 재생된 노래 순으로 정렬하고, 최대 2개만 남긴다.
    result = []
    for genre, total_play in most_genres:
        best_songs = sorted(songs[genre], key = lambda x:x[1], reverse = True)[:2]
        for i, play in best_songs:
            result.append(i)

    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.05ms, 10.1MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.05ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.05ms, 10.4MB)
테스트 14 〉	통과 (0.05ms, 10MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
"""