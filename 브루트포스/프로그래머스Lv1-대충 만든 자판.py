def solution(keymap, targets):
    keytable = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in keytable:
                keytable[key] = i + 1
            else:
                keytable[key] = min(keytable[key], i + 1)
    
    result = []
    for target in targets:
        clicked = 0
        for key in target:
            if key not in keytable:
                clicked = -1
                break
            clicked += keytable[key]
        result.append(clicked)
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.12ms, 10.1MB)
테스트 2 〉	통과 (0.12ms, 10.1MB)
테스트 3 〉	통과 (0.08ms, 9.95MB)
테스트 4 〉	통과 (0.15ms, 10.2MB)
테스트 5 〉	통과 (0.09ms, 10.1MB)
테스트 6 〉	통과 (0.16ms, 10.2MB)
테스트 7 〉	통과 (0.11ms, 10.1MB)
테스트 8 〉	통과 (0.12ms, 10.1MB)
테스트 9 〉	통과 (0.16ms, 10.1MB)
테스트 10 〉	통과 (0.10ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 10.1MB)
"""