"""
--input--
4 4      # n x m 의 형태
1 1 0    # (1,1)에서 시작하고 방향은 0(북쪽)
1 1 1 1  # 바다 바다 바다 바다
1 0 0 1  # 바다 육지 육지 바다
1 1 0 1  # 바다 바다 육지 바다
1 1 1 1  # 바다 바다 바다 바다

방향은 숫자로 표현된다
북: 0, 동: 1, 남: 2, 서: 3

1. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 확인한다.
2. 가보지 않은 칸이라면 한 칸 이동하고 가보지 않은 칸이라면 다시 1번으로 돌아간다.
3. 4방향을 모두 확인했을 때, 모두 가본 칸이거나 바다라면 방향을 유지한채로 1칸 후진한다.
    그리고 1번으로 돌아간다. 만약 후진할 칸이 바다라면 움직임을 멈춘다.

캐릭터가 방문한 칸의 수를 출력하라(단, 맨 처음 시작은 무조건 육지다.)
"""
import sys
input = lambda : sys.stdin.readline().rstrip()
n, m = map(int, input().split())
y, x, direction = map(int, input().split())

# 맵 정보
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 방문 정보, 첫번째 칸은 방문처리
visited = [[0] * m for _ in range(n)]
visited[y][x] = 1

# 방향정보
d = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}
# 방향전환
def turn_left():
    global direction, turn_count
    direction -= 1
    if direction == -1:
        direction = 3
    turn_count += 1

result = 1
turn_count = 0

while True:
    turn_left()
    dy, dx = d[direction]
    ny, nx = y + dy, x + dx
    if array[ny][nx] == 0 and not visited[ny][nx]:
        visited[ny][nx] = 1 #방문처리
        x, y = nx, ny       #위치이동
        result += 1         #결과값 + 1
        turn_count = 0      #turn횟수 초기화
        continue

    if turn_count == 4:
        ny, nx = y - dy, x - dx
        if array[ny][nx] == 1:
            break
        x, y = nx, ny
        turn_count = 0

print(result)

"""
5 5
1 1 0
1 1 1 1 1
1 0 0 1 1
1 1 0 0 1
1 0 0 0 1
1 1 1 1 1

-> 7
"""