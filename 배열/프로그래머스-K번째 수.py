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