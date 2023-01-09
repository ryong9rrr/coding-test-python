def initialize():
    table = {}
    ascii_code = 65
    while ascii_code <= 90:
        table[chr(ascii_code)] = ascii_code - 65 + 1
        ascii_code += 1
    return table, ascii_code - 65 + 1

def LZW(word):
    table, index = initialize()
    
    def find(word):
        stack = list(word)
        while stack:
            w = "".join(stack)
            if w in table:
                return w
            stack.pop()
        return None
    
    result = []
    while word:
        w = find(word)
        if not w:
            break
        result.append(table[w])
        word = word.replace(w, "", 1)
        if not word:
            break
        next_key = w + word[0]
        table[next_key] = index
        index += 1
    return result
    

def solution(msg):
    return LZW(msg)

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (46.13ms, 10.4MB)
테스트 5 〉	통과 (0.17ms, 10.2MB)
테스트 6 〉	통과 (301.19ms, 10.2MB)
테스트 7 〉	통과 (75.43ms, 10.2MB)
테스트 8 〉	통과 (157.41ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (160.63ms, 10.2MB)
테스트 11 〉	통과 (47.87ms, 10.3MB)
테스트 12 〉	통과 (264.00ms, 10.2MB)
테스트 13 〉	통과 (541.78ms, 10.3MB)
테스트 14 〉	통과 (483.15ms, 10.2MB)
테스트 15 〉	통과 (556.45ms, 10.3MB)
테스트 16 〉	통과 (214.07ms, 10.2MB)
테스트 17 〉	통과 (205.62ms, 10.2MB)
테스트 18 〉	통과 (11.98ms, 10.2MB)
테스트 19 〉	통과 (24.99ms, 10.2MB)
테스트 20 〉	통과 (153.18ms, 10.4MB)
"""