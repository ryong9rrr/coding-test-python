# 📖 팀 노트

# 출력

## sep

```python
print("Hello", "World")
# Hello World

print("Hello", "World", sep = ",")
# Hello,World

print("Hello","World", sep="\n")
# Hello
# World
```

## end

```python
print("Hello", end=" ")
print("World")
# Hello World
```

## f-string

```python
idx = 1
name = "yong"
print(f"{idx} : {name}")
# 1 : yong
```

# 입력

## import sys

`input()`을 아래처럼 정의하면 좋다.

다만 개행문자(`\n`)까지 출력하기 때문에 `rstrip()` 을 붙여주자

```python
import sys
input = sys.stdin.readline
a = input().rstrip()
```

## 여러개 입력하기

입력형식 : 띄어쓰기

```python
a, b, c = input().split()
```

## 정수 여러개 입력하기(map)

`map`을 이용해 입력 값 정수로 변환하기

```python
a, b, c = map(int, input().split())
```

# 수 / 문자

## 진수 표현

```python
a = 10
# 10 (a는 정수)
b = 10.0
# 10.0 (b는 실수)
c = 0o17
# 15 (8진수로 입력, 10진수로 반환)
d = 0x1f
# 31 (16진수로 입력, 10진수로 반환)
```

## 진수변환

```python
# 10진수 -> 16진수
print("%x"%15)
#f
print("%X"%15)
#F

# 10진수 -> 8진수
print("%o"%9)
#11

# 16진수 -> 10진수
x = int("ff", 16)
print(x)
# 255

# 8진수 -> 10진수
x = int("11", 8)
print(x)
# 9
```

## 비트단위연산

### bool

python에서 정수값 0은 `False` 임.

python에서 !은 not으로 한다.

```python
bool(0)
# False
not bool(0)
# True
!bool(0)
# 잘못된 표현
```

### AND / OR

비트단위 and 연산은 두 비트열이 주어졌을 때,
둘 다 1인 부분의 자리만 1로 만들어주는 것과 같다.

이 연산을 이용하면 어떤 비트열의 특정 부분만 모두 0으로도 만들 수 있는데
192.168.0.31 : 11000000.10101000.00000000.00011111
255.255.255.0 : 11111111.11111111.11111111.00000000

두 개의 ip 주소를 & 연산하면
192.168.0.0 : 110000000.10101000.0000000.00000000 을 계산할 수 있다.

실제로 이 계산은 네트워크에 연결되어 있는 두 개의 컴퓨터가 데이터를 주고받기 위해
같은 네트워크에 있는지 아닌지를 판단하는데 사용된다.

이러한 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서
마스크연산(특정 부분을 가리고 출력하는)을 수행하는 데에도 효과적으로 사용된다.

```python
3 & 5 (0b11 & 0b101 -> 0b1)
# 1
3 | 5 (0b11 & 0b101 -> 0b111)
# 7
```

### XOR (배타적 OR)

bool 과 정수에서 사용할 수 있다.

정수일 경우 2진법으로 변환되어 XOR연산을 수행한다.

이러한 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서도 효과적으로 사용된다.

구체적으로 설명하자면,
두 장의 이미지가 겹쳐졌을 때 색이 서로 다른 부분만 처리할 수 있다.
배경이 되는 그림과 배경 위에서 움직이는 그림이 있을 때,
두 그림에서 차이만 골라내 배경 위에서 움직이는 그림의 색으로 바꿔주면
전체 그림을 구성하는 모든 점들의 색을 다시 계산해 입히지 않고
보다 효과적으로 그림을 처리할 수 있게 되는 것이다.
비행기 슈팅게임 등을 상상해보면 된다.

```python
bool(1)^bool(0)
# True

3^5 (0b11^0b101 -> 0b110)
# 0b110(2진수) = 6(10진수)
```

### ~ (비트 NOT 연산자, 보수)

아래는 "2진수"에서의 보수표현

2진수에서는 `~n = -n-1`이 성립한다.

```
(ex. 4bit)
+7 0111
+6 0110
+5 0101
+4 0100
+3 0011
+2 0010
+1 0001
 0 0000
------------ ~(0001) = 1110 ... => ~n = -n-1
-1 1111
-2 1110
-3 1101
-4 1100
-5 1011
-6 1010
-7 1001
-8 1000
```

### 비트시프트

```python
10>>1
# 5
10<<1
# 20
0o17>>1
# 7
0o17<<1
# 30
0x1f>>1
# 15
0o17<<1
# 62
0o17<<2
# 124
```

## 유니코드

```python
# 문자 -> 숫자
number = ord("A")
print(number)
# 65

# 숫자 -> 문자
s = chr(65)
print(s)
# A
```

## 반올림(format, round)

```python
print(format(3.141592, ".2f"))
# 3.14
print(round(3.141592, 2))
# 3.14
```

## 문자열 뒤집기

```python
a = "abcdefg"
print(a[::-1])
# gfedcba
```

## 문자열에 앞에 "0" 채우기 (zfill)

`문자열.zfill(범위)`

```python
print("1".zfill(4))
# 0001
print("111".zfill(4))
# 0111
```

## 문자열에 앞에 특정문자 채우기 (rjust)

`rjust()`는 특정문자를 지정할 수 있다.

```python
print("1".rjust(4, "a"))
# aaa1
print("111".rjust(6, "2"))
# 222111
```

## 특정문자 찾기

### find(찾을문자, 찾기시작할위치)

find는 문자열중에 특정문자를 찾고 위치를 반환해준다, 없을경우 -1을 리턴

```python
>>> s = '가나다라 마바사아 자차카타 파하'
>>> s.find('마')
5
>>> s.find('가')
0
>>> s.find('가',5)
-1
```

### startswith(시작하는문자, 시작지점)

```python
>>> s = '가나다라 마바사아 자차카타 파하'
>>> s.startswith('가')
True
>>> s.startswith('마')
False

>>> s.startswith('마',s.find('마')) #find는 '마' 의 시작지점을 알려줌 : 5
True
>>> s.startswith('마',1)
False
```

### endswith(끝나는문자, 문자열의시작, 문자열의끝)

```python
>>> s = '가나다라 마바사아 자차카타 파하'
>>> s.endswith('마')
False
>>> s.endswith('하')
True

>>> s.endswith('마',0,10)
False
>>> s.endswith('마',0,6)
True
```

# 다익스트라

한 노드에서 다른 모든 노드로 가는 비용문제

```python
import heapq

INF = int(1e9)

# node num
n = 6
# edge num
m = 11

# node info
graph = [
    [],
    [(2, 2), (3, 5), (4, 1)],
    [(1, 2), (3, 3), (4, 2)],
    [(1, 5), (2, 3), (4, 3), (5, 1), (6, 5)],
    [(1, 1), (2, 2), (3, 3), (5, 1)],
    [(3, 1), (4, 1), (6, 2)],
    [(3, 5), (5, 2)]
]

# check visited
visited = [False] * (n + 1)

# distance
distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # if q is not empty
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, d in graph[now]:
            cost = dist + d
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))

dijkstra(1)

print(distance[1:])
# [0, 2, 3, 1, 2, 4]
```

# 플로이드 와샬

```python
INF = int(1e9)

#node num
n = 4
graph = [
    [],
    [INF, 0, 5, INF, 8],
    [INF, 7, 0, 9, INF],
    [INF, 2, INF, 0, 4],
    [INF, INF, INF, 3, 0]
]

def fw():
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min( graph[a][b], graph[a][k]+graph[k][b] )

fw()
for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end=" ")
    print()

"""
0 5 11 8
7 0 9 13
2 7 0 4
5 10 3 0
"""
```

# 힙

```python
# heap
class BinaryHeap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    # insert heapify
    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = \
                    self.items[i], self.items[parent]
            i = parent
            parent = i // 2

    # insert, this is heapq.heappush()
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    # pop heapify
    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
        if smallest != idx:
            self.items[idx], self.items[smallest] = \
                self.items[smallest], self.items[idx]
            self._percolate_down(smallest)

    # extract, this is heapq.heappop()
    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted


numbers = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

heap = BinaryHeap()

for number in numbers:
    heap.insert(number)

print(heap.items)
# [None, 1, 2, 4, 3, 8, 6, 5, 10, 7, 9]

for _ in range(len(numbers)):
    print(heap.extract(), end=" ")
# 1 2 3 4 5 6 7 8 9 10
```

# 정렬 알고리즘

## 선택정렬(selection-sort)

```python
n = 10
numbers = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(n):
    #once, set front number is the min number.
    min_index = i
    #search next number
    for j in range(i+1, n):
        if numbers[min_index] > numbers[j]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## 버블정렬(bubble-sort)

```python
n = 10
numbers = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(1, n):
    for j in range(0, n-1):
        if numbers[j] > numbers [j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## 삽입정렬(insert-sort)

```python
n = 10
numbers = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(1, n):
    for j in range(i, 0, -1):
        if numbers[j-1] > numbers[j] :
            numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
        else:
            break
print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## 퀵정렬(quick-sort)

```python
def quicksort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while start < right and array[pivot] <= array[right]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quicksort(array, start, right - 1)
    quicksort(array, right + 1, end)

n = 10
numbers = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

quicksort(numbers, 0, n-1)

print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## 병합정렬(merge-sort)

```python
def merge(list, left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        list[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        list[k] = right[j]
        j += 1
        k += 1

def merge_sort(list):
    n = len(list)
    if n <= 1:
        return
    mid = n // 2
    left = list[:mid]
    right = list[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(list, left, right)

numbers = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

merge_sort(numbers)

print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

# 위상정렬

```python
from collections import deque

graph = {
    1: [2, 5],
    2: [3],
    3: [4],
    4: [6],
    5: [6],
    6: [7],
    7: []
}
n = len(graph)

def topology_sort(n:int, graph:dict)->list:
    INF = 987654321
    result = []
    degree = [INF] + [0 for _ in range(n)]
    q = deque()

    # insert degree info in list
    for nodes in graph.values():
        for node in nodes:
            degree[node] += 1

    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)

    for _ in range(n):
        if len(q) == 0:
            print("occur cycle..")
            return
        x = q.popleft()
        result.append(x)
        for node in graph[x]:
            degree[node] -= 1
            if degree[node] == 0:
                q.append(node)

    return result

print(topology_sort(n, graph))
# [1, 2, 5, 3, 4, 6, 7]
```

# Union-Find

```python
def find_parent(array:list, x:int)->int:
    if array[x] != x:
        array[x] = find_parent(array, array[x])
    return array[x]

def union_parent(array:list, a:int, b:int):
    a = find_parent(array, a)
    b = find_parent(array, b)
    if a < b:
        array[b] = a
    else:
        array[a] = b

def check_parent(array:list, a:int, b:int)->bool:
    a = find_parent(array, a)
    b = find_parent(array, b)
    if a == b:
        return True
    else:
        return False

# node num
n = 8

# node init as index
parent = [x for x in range(n+1)]

union_parent(parent, 1, 2)
union_parent(parent, 2, 3)
union_parent(parent, 3, 4)
union_parent(parent, 5, 6)
union_parent(parent, 6, 7)
union_parent(parent, 7, 8)

print(parent[1:])
# [1, 1, 1, 1, 5, 5, 5, 5]

print(check_parent(parent, 1, 5))
# False
```

SCC (강한결합요소)

```python
from collections import deque
# graph info
n = 11
graph = {
    1: [2],
    2: [3],
    3: [1],
    4: [2, 5],
    5: [7],
    6: [5],
    7: [6],
    8: [5, 9],
    9: [10],
    10: [11],
    11: [3, 8],
}

stack = deque()
d = [0] * (n+1)
finished = [False] * (n+1)
SCC = []

def dfs(x:int)->int:
    d[x] = x
    stack.append(x)

    parent = d[x]
    for i, v in enumerate(graph[x]):
        node = v
        if d[node] == 0:
            parent = min(parent, dfs(node))
        elif not finished[node]:
            parent = min(parent, d[node])

    if parent == d[x]:
        scc = []
        while True:
            t = stack.pop()
            scc.append(t)
            finished[t] = True
            if t == x:
                break
        SCC.append(scc)

    return parent

for i in range(1, n+1):
    if d[i] == 0 :
        dfs(i)

print(stack)
print(d)
print(finished)
print(SCC)
"""
deque([])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[False, True, True, True, True, True, True, True, True, True, True, True]
[[3, 2, 1], [6, 7, 5], [4], [11, 10, 9, 8]]
"""
```

# 최대유량문제

```python
from collections import deque

n = 6
INF = int(1e9)
# (vertex, capacity)
graph = {
    1: [(2, 12), (4, 11)],
    2: [(3, 6), (4, 5), (5, 5), (6, 9)],
    3: [(6, 8)],
    4: [(5, 9)],
    5: [(3, 3), (6, 4)],
    6: []
}

nodes = dict()
c = [None] + [[0]*100 for _ in range(n)]
f = [None] + [[0]*100 for _ in range(n)]

# manufacturing data...
for i, info in enumerate(graph.values()):
    node_list = []
    node = i + 1
    for vertex, capacity in info:
        node_list.append(vertex)
        c[node][vertex] = capacity
    nodes[node] = node_list

# {1: [2, 4], 2: [3, 4, 5, 6], 3: [6], 4: [5], 5: [3, 6], 6: []} // nodes
# [None, [0, 0, 12, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0... // capacity

def max_flow(start:int, end:int, n:int)->int:
    result = 0
    while True:
        d = [-1] * (n + 1)
        q = deque()
        q.append(start)
        while q:
            x = q.popleft()
            for node in nodes[x]:
                if c[x][node] - f[x][node] > 0 and d[node] == -1:
                    q.append(node)
                    d[node] = x
                    if node == end:
                        break
        if d[end] == -1:
            break
        flow = INF
        i = end
        while i != start:
            flow = min(flow, c[d[i]][i] - f[d[i]][i])
            i = d[i]

        i = end
        while i != start:
            f[d[i]][i] += flow
            f[i][d[i]] -= flow
            i = d[i]

        result += flow

    return result

print(max_flow(1, 6, n))
# 19
```
