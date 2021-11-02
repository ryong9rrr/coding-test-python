def solution(array, commands):
    result = []
    for command in commands :
        [i, j, k] = command
        result.append( sorted(array[i-1:j])[k-1] )
        
    return result

"""js
function solution(array, commands) {
  return commands.map((command) => {
    const [i, j, k] = command;
    return array.slice(i - 1, j).sort((a, b) => a - b)[k - 1];
  });
}
"""
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
"""