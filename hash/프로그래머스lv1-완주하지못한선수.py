from collections import defaultdict
def solution(participant, completion):
    table = defaultdict(int)
    
    for person in completion:
        table[person] += 1
    
    for person in participant:
        if person not in table or table[person] == 0:
            return person
        table[person] -= 1

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.14ms, 10.1MB)
테스트 4 〉	통과 (0.35ms, 10.3MB)
테스트 5 〉	통과 (0.28ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (19.51ms, 21.7MB)
테스트 2 〉	통과 (35.41ms, 25.1MB)
테스트 3 〉	통과 (37.48ms, 27.5MB)
테스트 4 〉	통과 (38.35ms, 34MB)
테스트 5 〉	통과 (60.18ms, 33.9MB)
"""

# Counter 사용
from collections import Counter
def solution(participant, completion):
    part = Counter(participant)
    com = Counter(completion)
    
    for key in part.keys():
        if not com[key]:
            return key
        com[key] -= part[key]
        if com[key] < 0:
            return key

"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.18ms, 10.4MB)
테스트 4 〉	통과 (0.67ms, 10.4MB)
테스트 5 〉	통과 (0.28ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (20.80ms, 24.4MB)
테스트 2 〉	통과 (42.82ms, 27.8MB)
테스트 3 〉	통과 (41.13ms, 30.2MB)
테스트 4 〉	통과 (45.21ms, 39MB)
테스트 5 〉	통과 (31.45ms, 38.9MB)
"""

"""
js // forEach는 return 값이 undefined라서 사용하면 안됨. 그래서 for-of 사용

function solution(participant, completion) {
    const table = completion.reduce((obj, person) =>{
        if (!obj[person]){
            obj[person] = 0;
        }
        obj[person]++;
        return obj
    }, {})
    
    for (const person of participant) {
        if (person in table){
            table[person] -= 1;
        } else {
            return person
        }
        
        if (table[person] < 0) return person
    }
}

정확성  테스트
테스트 1 〉	통과 (0.25ms, 30.1MB)
테스트 2 〉	통과 (0.21ms, 30.1MB)
테스트 3 〉	통과 (0.38ms, 30MB)
테스트 4 〉	통과 (0.49ms, 30.2MB)
테스트 5 〉	통과 (0.49ms, 30.1MB)
효율성  테스트
테스트 1 〉	통과 (40.03ms, 45.7MB)
테스트 2 〉	통과 (50.36ms, 51.2MB)
테스트 3 〉	통과 (53.86ms, 54.4MB)
테스트 4 〉	통과 (59.00ms, 61.1MB)
테스트 5 〉	통과 (63.32ms, 64.3MB)
"""