# 다익스트라 문제
from collections import defaultdict, deque
def solution(n, edge):
    graph = defaultdict(list)
    # 양방향 그래프 구성
    for v, w in edge:
        graph[v].append(w)
        graph[w].append(v)
    
    # 노드에 방문했을 때의 최단거리를 담는다.
    visited = [0] * (n + 1)
    q = deque()
    q.append((1, 1)) #(v, distance)
    # bfs 시작
    while q:
        v, distance = q.popleft()
        if visited[v]:
            continue
        visited[v] += distance
        for w in graph[v]:
            # 방문하지 않은 노드만 방문(양방향 그래프라서)
            if not visited[w]:
                q.append((w, distance + 1))
    
    return visited.count(max(visited))

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.47ms, 10.3MB)
테스트 5 〉	통과 (1.78ms, 10.6MB)
테스트 6 〉	통과 (2.77ms, 11.2MB)
테스트 7 〉	통과 (26.76ms, 18.7MB)
테스트 8 〉	통과 (39.80ms, 20.9MB)
테스트 9 〉	통과 (47.83ms, 22.5MB)


js, 파이썬과 동일한 풀이, 시간이 엄청 오래걸리는데, shift 사용때문으로 보임
function makeGraph(vertexArray){
    const graph = {};
    for (const [v, w] of vertexArray){
        if (!graph[v]) graph[v] = [];
        if (!graph[w]) graph[w] = [];
        graph[v].push(w)
        graph[w].push(v)
    }
    return graph
}

function solution(n, edge) {
    const graph = makeGraph(edge);
    const visited = Array.from({length : n + 1}, v => 0);
    const q = [];
    
    q.push([1, 1])
    while (q.length > 0){
        const [v, distance] = q.shift();
        if (visited[v]) continue;
        visited[v] += distance;
        for (const w of graph[v]){
            if (visited[w]) continue;
            q.push([w, distance + 1]);
        }
    }
    
    const maxDistance = Math.max(...visited);
    return visited.filter(v => v === maxDistance).length
}

정확성  테스트
테스트 1 〉	통과 (0.33ms, 29.9MB)
테스트 2 〉	통과 (0.40ms, 30MB)
테스트 3 〉	통과 (0.42ms, 30MB)
테스트 4 〉	통과 (0.75ms, 30.1MB)
테스트 5 〉	통과 (2.02ms, 30.4MB)
테스트 6 〉	통과 (17.07ms, 35.1MB)
테스트 7 〉	통과 (84.55ms, 48.1MB)
테스트 8 〉	통과 (42.92ms, 55.5MB)
테스트 9 〉	통과 (7621.53ms, 57.5MB)


// 직접 구현한 큐, 효과는 굉장했다.
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.front = this.tail = null;
    this.size = 0;
  }

  get peek() {
    return (this.front && this.front.value) || null;
  }

  enqueue(newValue) {
    const newNode = new Node(newValue);
    if (!this.front) {
      this.front = this.tail = newNode;
    } else {
      this.tail = this.tail.next = newNode;
    }
    this.size++;
  }

  dequeue() {
    if (!this.front) return null;
    const extracted = this.front.value;
    this.front = this.front.next;
    this.size--;
    return extracted;
  }
}

function makeGraph(vertexArray) {
  const graph = {};
  for (const [v, w] of vertexArray) {
    if (!graph[v]) graph[v] = [];
    if (!graph[w]) graph[w] = [];
    graph[v].push(w);
    graph[w].push(v);
  }
  return graph;
}

function solution(n, edge) {
  const graph = makeGraph(edge);
  const visited = Array.from({ length: n + 1 }, (v) => 0);
  const q = new Queue();

  q.enqueue([1, 1]);
  while (q.size > 0) {
    const [v, distance] = q.dequeue();
    if (visited[v]) continue;
    visited[v] += distance;
    for (const w of graph[v]) {
      if (visited[w]) continue;
      q.enqueue([w, distance + 1]);
    }
  }

  const maxDistance = Math.max(...visited);
  return visited.filter((v) => v === maxDistance).length;
}

/*
정확성  테스트
테스트 1 〉	통과 (0.69ms, 29.9MB)
테스트 2 〉	통과 (0.43ms, 29.8MB)
테스트 3 〉	통과 (0.51ms, 30.1MB)
테스트 4 〉	통과 (0.91ms, 30.2MB)
테스트 5 〉	통과 (2.79ms, 30.6MB)
테스트 6 〉	통과 (23.60ms, 35MB)
테스트 7 〉	통과 (40.86ms, 48.4MB)
테스트 8 〉	통과 (59.49ms, 57MB)
테스트 9 〉	통과 (69.90ms, 58.8MB)
"""