# dfs로 풀기
def solution(numbers, target):
    count = 0
    
    def dfs(total, index):
        nonlocal count
        if index < len(numbers):
            dfs(total + numbers[index], index + 1)
            dfs(total - numbers[index], index + 1)
            return
        elif index == len(numbers) and total == target:
            count += 1
            return
        return
    
    dfs(0, 0)
    return count

"""
정확성  테스트
테스트 1 〉	통과 (409.96ms, 10.2MB)
테스트 2 〉	통과 (381.63ms, 10.2MB)
테스트 3 〉	통과 (0.41ms, 10.2MB)
테스트 4 〉	통과 (1.50ms, 10.2MB)
테스트 5 〉	통과 (11.80ms, 10.2MB)
테스트 6 〉	통과 (0.76ms, 10.2MB)
테스트 7 〉	통과 (0.40ms, 10.2MB)
테스트 8 〉	통과 (5.21ms, 10.2MB)
"""

# itertools.product 순열 구해서 풀기
from itertools import product
def solution(numbers, target):
    nums = [(x, -x) for x in numbers]
    p = list(product(*nums))
    return [sum(arr) for arr in p].count(target)

"""
정확성  테스트
테스트 1 〉	통과 (607.69ms, 258MB)
테스트 2 〉	통과 (619.32ms, 258MB)
테스트 3 〉	통과 (0.45ms, 10.3MB)
테스트 4 〉	통과 (2.39ms, 10.8MB)
테스트 5 〉	통과 (14.93ms, 16.4MB)
테스트 6 〉	통과 (0.78ms, 10.3MB)
테스트 7 〉	통과 (0.37ms, 10.3MB)
테스트 8 〉	통과 (3.58ms, 11.5MB)
"""


"""js
function solution(numbers, target) {
    let count = 0;
    
    function dfs(total, index){
        if (index < numbers.length){
            dfs(total + numbers[index], index + 1);
            dfs(total - numbers[index], index + 1);
            return;
        }
        else if (index === numbers.length && total === target){
            return count++;
        }
    }
    
    dfs(0, 0)
    
    return count
}

정확성  테스트
테스트 1 〉	통과 (14.44ms, 32.7MB)
테스트 2 〉	통과 (13.42ms, 32MB)
테스트 3 〉	통과 (0.22ms, 30.4MB)
테스트 4 〉	통과 (1.30ms, 32.1MB)
테스트 5 〉	통과 (2.36ms, 31.9MB)
테스트 6 〉	통과 (0.36ms, 30.2MB)
테스트 7 〉	통과 (0.23ms, 30.2MB)
테스트 8 〉	통과 (1.90ms, 32MB)
"""