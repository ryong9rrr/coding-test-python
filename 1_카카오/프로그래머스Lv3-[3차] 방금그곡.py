import functools

def convert_time(time):
    hour, minute = time.split(":")
    return 60 * int(hour) + int(minute)

def interval_minute(start_time, end_time):
    return convert_time(end_time) - convert_time(start_time)

def get_running_sheet(sheet, running_minute):
    length = len(sheet)
    if length == running_minute:
        return sheet
    if running_minute < length:
        return sheet[:running_minute]
    a, b = divmod(running_minute, length)
    return sheet * a + sheet[:b]

def replace_molody(melody):
    special_melodies = [
        ["C#", "c"],
        ["D#", "d"],
        ["F#", "f"],
        ["G#", "g"],
        ["A#", "a"],
      ]
    for origin, replaced in special_melodies:
        melody = melody.replace(origin, replaced)
    return melody

def compare(a, b):
    if a[0] == b[0]:
        return a[1] - b[1]
    return b[0] - a[0]

def solution(m, musicinfos):
    target = replace_molody(m)
    result = []
    
    for i, musicinfo in enumerate(musicinfos):
        start_time, end_time, title, origin_sheet = musicinfo.split(",")
        sheet = replace_molody(origin_sheet)
        running_minute = interval_minute(start_time, end_time)
        running_sheet = get_running_sheet(sheet, running_minute)
        if target in running_sheet:
            result.append([running_minute, i, title])
        
    if not result:
        return "(None)"
    
    return sorted(result, key=functools.cmp_to_key(compare))[0][2]
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.04ms, 10.4MB)
테스트 6 〉	통과 (0.04ms, 10.4MB)
테스트 7 〉	통과 (0.08ms, 10.4MB)
테스트 8 〉	통과 (0.09ms, 10.4MB)
테스트 9 〉	통과 (0.07ms, 10.3MB)
테스트 10 〉	통과 (0.11ms, 10.3MB)
테스트 11 〉	통과 (0.09ms, 10.4MB)
테스트 12 〉	통과 (0.07ms, 10.4MB)
테스트 13 〉	통과 (0.10ms, 10.3MB)
테스트 14 〉	통과 (0.08ms, 10.5MB)
테스트 15 〉	통과 (0.08ms, 10.4MB)
테스트 16 〉	통과 (0.08ms, 10.5MB)
테스트 17 〉	통과 (0.08ms, 10.4MB)
테스트 18 〉	통과 (0.07ms, 10.5MB)
테스트 19 〉	통과 (0.13ms, 10.6MB)
테스트 20 〉	통과 (1.22ms, 10.3MB)
테스트 21 〉	통과 (0.08ms, 10.4MB)
테스트 22 〉	통과 (0.07ms, 10.4MB)
테스트 23 〉	통과 (0.12ms, 10.4MB)
테스트 24 〉	통과 (0.08ms, 10.4MB)
테스트 25 〉	통과 (0.04ms, 10.4MB)
테스트 26 〉	통과 (0.05ms, 10.6MB)
테스트 27 〉	통과 (0.05ms, 10.4MB)
테스트 28 〉	통과 (0.04ms, 10.4MB)
테스트 29 〉	통과 (1.29ms, 10.6MB)
테스트 30 〉	통과 (1.57ms, 10.6MB)
"""