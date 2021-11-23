// 최단경로 찾기, bfs 문제
function Graph() {
  this.edge = {};
  this.visited = {};
}

Graph.prototype.addVertex = function (v) {
  this.edge[v] = [];
  this.visited[v] = 0;
};

Graph.prototype.addEdge = function (v1, v2) {
  this.edge[v2].push(v1);
  this.edge[v1].push(v2);
};

function solution(n, edge) {
  var answer = 0;

  // 1. graph 설정
  let g = new Graph();
  for (let i = 1; i <= n; i++) {
    g.addVertex(i);
  }

  for (let i = 0; i < edge.length; i++) {
    g.addEdge(edge[i][0], edge[i][1]);
  }

  // 2. bfs
  let q = [];
  q.push([1, 1]);
  g.visited[1] = 0;
  while (q.length != 0) {
    let [n, c] = q.shift();

    if (g.visited[n]) continue;

    g.visited[n] = c;
    for (let i = 0; i < g.edge[n].length; i++) {
      if (!g.visited[g.edge[n][i]]) {
        q.push([g.edge[n][i], c + 1]);
      }
    }
  }

  // 3. 가장 먼 경로 확인 후 노드 반환
  let d = Object.values(g.visited);
  let max = Math.max(...d);

  return d.reduce((pre, v) => pre + (v === max ? 1 : 0), 0);

  return answer;
}
/*
정확성  테스트
테스트 1 〉	통과 (0.35ms, 30.3MB)
테스트 2 〉	통과 (0.42ms, 30.4MB)
테스트 3 〉	통과 (0.52ms, 30MB)
테스트 4 〉	통과 (0.59ms, 30.3MB)
테스트 5 〉	통과 (1.79ms, 30.3MB)
테스트 6 〉	통과 (9.20ms, 33.1MB)
테스트 7 〉	통과 (75.27ms, 48.7MB)
테스트 8 〉	통과 (30.85ms, 53.9MB)
테스트 9 〉	통과 (166.37ms, 54MB)
*/

// 최적화
function Graph() {
  this.edge = {};
  this.visited = {};
}

Graph.prototype.addVertex = function (v) {
  this.edge[v] = [];
  this.visited[v] = 0;
};

Graph.prototype.addEdge = function (v1, v2) {
  this.edge[v2].push(v1);
  this.edge[v1].push(v2);
};

function solution(n, edge) {
  var answer = 0;

  // 1. graph 설정
  let g = new Graph();
  for (let i = 1; i <= n; i++) {
    g.addVertex(i);
  }

  for (let i = 0; i < edge.length; i++) {
    g.addEdge(edge[i][0], edge[i][1]);
  }

  // 2. bfs
  let q = [];
  let head = 0,
    tail = 0,
    max = 0;
  q[tail++] = [1, 1];
  g.visited[1] = 0;
  while (head != tail) {
    let [n, c] = q[head++];

    if (g.visited[n]) continue;

    g.visited[n] = c;
    if (c > max) max = c;
    for (let i = 0; i < g.edge[n].length; i++) {
      if (!g.visited[g.edge[n][i]]) {
        q[tail++] = [g.edge[n][i], c + 1];
      }
    }
  }

  // 3. 가장 먼 경로 확인 후 노드 반환
  return Object.values(g.visited).reduce(
    (pre, v) => pre + (v === max ? 1 : 0),
    0
  );

  return answer;
}
/*
정확성  테스트
테스트 1 〉	통과 (0.22ms, 30.2MB)
테스트 2 〉	통과 (0.40ms, 30.4MB)
테스트 3 〉	통과 (0.39ms, 30.2MB)
테스트 4 〉	통과 (0.69ms, 30.4MB)
테스트 5 〉	통과 (3.29ms, 30.3MB)
테스트 6 〉	통과 (13.54ms, 33.6MB)
테스트 7 〉	통과 (38.47ms, 49.5MB)
테스트 8 〉	통과 (32.94ms, 54.2MB)
테스트 9 〉	통과 (26.24ms, 54.3MB)
*/

// 참고) 인접리스트 초기화
const adjList = edges.reduce((G, [from, to]) => {
  G[from] = (G[from] || []).concat(to);
  G[to] = (G[to] || []).concat(from);
  return G;
}, {});
