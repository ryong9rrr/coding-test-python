// graph + dfs
function dfs(computers, visited, idx) {
  if (visited[idx]) {
    return 0;
  }

  visited[idx] = 1;

  for (let i = 0; i < computers[idx].length; i++) {
    if (computers[idx][i]) {
      dfs(computers, visited, i);
    }
  }
  return 1;
}

function solution(n, computers) {
  var answer = 0;

  let visited = new Array(n).fill(0);

  for (let i = 0; i < n; i++) {
    answer += dfs(computers, visited, i);
  }

  return answer;
}
