def solution(s):
    global count, removed_zero
    count = removed_zero = 0
    
    def change(binary):
        global count, removed_zero
        if binary == "1":
            return
        count += 1
        prev_length = len(binary)
        # next_length = len(binary.replace("0", "")) 와 같음.
        # 단순히 개수만 세주는 것이므로 시간이 더 빠르다.
        next_length = binary.count("1")
        removed_zero += (prev_length - next_length)
        change(bin(next_length)[2:])
    
    change(s)
    
    return [count, removed_zero]

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.13ms, 10.3MB)
테스트 10 〉	통과 (0.57ms, 10.2MB)
테스트 11 〉	통과 (0.17ms, 10.4MB)
"""