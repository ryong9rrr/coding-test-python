def solution(s):
    # 문자열를 단위만큼 쪼개서 list로 반환하는 함수
    def string_split(unit):
        result = []
        for i in range(0, len(s), unit):
            result.append(s[i:i + unit])
        return result
    
    # 처음 비교값은 s의 길이
    result = len(s)
    # 단위는 문자열의 절반만큼만 확인하면 된다.
    for unit in range(1, (len(s) // 2) + 1):
        arr = string_split(unit)
        std = arr[0]
        temp = ""
        count = 1
        for i in range(1, len(arr)):
            if std == arr[i]:
                count += 1
            else:
                if count > 1:
                    temp += str(count)
                    count = 1
                temp += std
                std = arr[i]
                    
        if count > 1:
            temp += str(count)
        temp += std
        
        if len(temp) < result:
            result = len(temp)
            
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.37ms, 10.2MB)
테스트 3 〉	통과 (0.36ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.08ms, 10.3MB)
테스트 7 〉	통과 (0.75ms, 10.4MB)
테스트 8 〉	통과 (0.42ms, 10.3MB)
테스트 9 〉	통과 (0.59ms, 10.2MB)
테스트 10 〉	통과 (2.41ms, 10.2MB)
테스트 11 〉	통과 (0.12ms, 10.3MB)
테스트 12 〉	통과 (0.17ms, 10.3MB)
테스트 13 〉	통과 (0.11ms, 10.2MB)
테스트 14 〉	통과 (0.58ms, 10.2MB)
테스트 15 〉	통과 (0.11ms, 10.4MB)
테스트 16 〉	통과 (0.02ms, 10.3MB)
테스트 17 〉	통과 (1.05ms, 10.3MB)
테스트 18 〉	통과 (1.02ms, 10.3MB)
테스트 19 〉	통과 (1.13ms, 10.3MB)
테스트 20 〉	통과 (2.40ms, 10.3MB)
테스트 21 〉	통과 (2.56ms, 10.2MB)
테스트 22 〉	통과 (2.61ms, 10.2MB)
테스트 23 〉	통과 (2.33ms, 10.4MB)
테스트 24 〉	통과 (2.12ms, 10.3MB)
테스트 25 〉	통과 (2.44ms, 10.3MB)
테스트 26 〉	통과 (2.32ms, 10.3MB)
테스트 27 〉	통과 (2.58ms, 10.3MB)
테스트 28 〉	통과 (0.02ms, 10.4MB)
"""

# 나랑 비슷하지만 조금 더 직관적인 풀이
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count > 1 else prev
        answer = min(answer, len(compressed))
        
    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.32ms, 10.4MB)
테스트 3 〉	통과 (0.16ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.37ms, 10.2MB)
테스트 8 〉	통과 (0.37ms, 10.2MB)
테스트 9 〉	통과 (0.54ms, 10.3MB)
테스트 10 〉	통과 (2.27ms, 10.4MB)
테스트 11 〉	통과 (0.08ms, 10.4MB)
테스트 12 〉	통과 (0.08ms, 10.2MB)
테스트 13 〉	통과 (0.10ms, 10.2MB)
테스트 14 〉	통과 (0.52ms, 10.3MB)
테스트 15 〉	통과 (0.09ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (1.06ms, 10.3MB)
테스트 18 〉	통과 (0.95ms, 10.3MB)
테스트 19 〉	통과 (1.06ms, 10.4MB)
테스트 20 〉	통과 (2.36ms, 10.2MB)
테스트 21 〉	통과 (2.33ms, 10.3MB)
테스트 22 〉	통과 (2.38ms, 10.3MB)
테스트 23 〉	통과 (2.27ms, 10.2MB)
테스트 24 〉	통과 (2.18ms, 10.4MB)
테스트 25 〉	통과 (2.37ms, 10.3MB)
테스트 26 〉	통과 (2.23ms, 10.3MB)
테스트 27 〉	통과 (2.21ms, 10.2MB)
테스트 28 〉	통과 (0.01ms, 10.2MB)
"""

"""js
// unit: number, s: string => string[]
function divideString(unit, s){
    let array = [];
    for (let i = 0; i < s.length; i += unit){
        array.push(s.slice(i, i + unit))
    }
    return array;
}

function solution(s) {
    let result = s.length;
    for (let unit = 1; unit < Math.floor(s.length / 2) + 1; unit++){
        const array = divideString(unit, s);
        let temp = ""
        let count = 1;
        let cur = array[0]
        for (let i = 1; i < array.length; i++){
            if (cur === array[i]){
                count++;
            } else {
                if (count > 1) temp += String(count)
                temp += cur
                cur = array[i]
                count = 1
            }
        }
        if (count > 1) temp += String(count)
        temp += cur
        if (result > temp.length){
            result = temp.length
        }
    }
    return result
}

정확성  테스트
테스트 1 〉	통과 (0.17ms, 30.2MB)
테스트 2 〉	통과 (0.30ms, 30.1MB)
테스트 3 〉	통과 (0.21ms, 30.4MB)
테스트 4 〉	통과 (0.20ms, 30.3MB)
테스트 5 〉	통과 (0.06ms, 30.3MB)
테스트 6 〉	통과 (0.13ms, 30.4MB)
테스트 7 〉	통과 (0.33ms, 30.4MB)
테스트 8 〉	통과 (0.34ms, 30.3MB)
테스트 9 〉	통과 (0.49ms, 30.3MB)
테스트 10 〉	통과 (3.18ms, 32.6MB)
테스트 11 〉	통과 (0.18ms, 30MB)
테스트 12 〉	통과 (0.19ms, 30.3MB)
테스트 13 〉	통과 (0.19ms, 30.4MB)
테스트 14 〉	통과 (0.42ms, 30.2MB)
테스트 15 〉	통과 (0.16ms, 30.2MB)
테스트 16 〉	통과 (0.12ms, 30.1MB)
테스트 17 〉	통과 (1.29ms, 32.9MB)
테스트 18 〉	통과 (1.32ms, 33.1MB)
테스트 19 〉	통과 (1.37ms, 32.8MB)
테스트 20 〉	통과 (2.01ms, 32.8MB)
테스트 21 〉	통과 (1.94ms, 32.8MB)
테스트 22 〉	통과 (1.96ms, 32.7MB)
테스트 23 〉	통과 (1.97ms, 33MB)
테스트 24 〉	통과 (1.89ms, 32.7MB)
테스트 25 〉	통과 (1.94ms, 32.2MB)
테스트 26 〉	통과 (1.91ms, 32.9MB)
테스트 27 〉	통과 (2.00ms, 32.8MB)
테스트 28 〉	통과 (0.13ms, 30.2MB)
"""