"""js
[Error]: Maximum call stack size exceeded
에러가 남.. 더 좋은 로직을 찾아봐야한다.
function dfs(numbers, target, index, total) {
  if (numbers.length === index) {
    return target === total ? 1 : 0;
  }

  let count = 0;
  count += dfs(numbers, target, index + 1, total + numbers[index]);
  count += dfs(numbers, target, index - 1, total - numbers[index]);

  return count;
}

function solution(numbers, target) {
  return dfs(numbers, target, 0, 0);
}
"""

#고생(풀다 만)의 흔적 ... dfs가 아니라 bfs가 맞는거 같은데..
import sys
sys.setrecursionlimit(10**6)
result = 0
def dfs(i:int, total:int, c:list, target:int, n:int):
    global result
    # breaking
    if n == 0:
        if total == target:
            return 1
        return 0
    # 인덱스는 50까지만 확인
    if i > 50:
        return
    # 방문을 다해서 숫자가 남아있지 않다면 다음 인덱스로 이동(이러면 똑같은거만봄...안됨)
    if not c[i]:
        dfs(i+1, total, c, target, n)
    
    #방문처리
    c[i] -= 1
    n -= 1
    #+,- 두갈래로 이동하는데..
    if not total + i >= target:
        dfs(i, total+i, c, target, n)
    if not total - i <= target:
        dfs(i, total-i, c, target, n)
        


def solution(numbers, target):
    global result
    c = [0] * 51
    n = len(numbers)
    for number in numbers:
        c[number] += 1
    
    total = 0
    dfs(0, total, c, target, n)
        
    return result

"""
👆 과거의 나는 대체 왜 이렇게 접근했을까...??? 대체 왜...?
"""

# dfs로 풀기
import sys
sys.setrecursionlimit(10**6)
def solution(numbers, target):
    count = 0
    n = len(numbers)
    
    def dfs(csum, index):
        nonlocal count
        if index == n and csum == target:
            count += 1
            return
        if index >= n:
            return
        dfs(csum + numbers[index], index+1)
        dfs(csum - numbers[index], index+1)
    
    dfs(0, 0)
    
    return count
"""
정확성  테스트
테스트 1 〉	통과 (363.45ms, 10.2MB)
테스트 2 〉	통과 (336.92ms, 10.2MB)
테스트 3 〉	통과 (0.32ms, 10.2MB)
테스트 4 〉	통과 (1.44ms, 10.2MB)
테스트 5 〉	통과 (10.15ms, 10.2MB)
테스트 6 〉	통과 (0.64ms, 10.2MB)
테스트 7 〉	통과 (0.34ms, 10.2MB)
테스트 8 〉	통과 (2.49ms, 10.2MB)
"""