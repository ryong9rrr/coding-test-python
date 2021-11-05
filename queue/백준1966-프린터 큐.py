from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
answer = []
for _ in range(N):
    n, target_i = map(int, input().split())
    papers = list(map(int, input().split()))

    q = deque()

    for paper in papers:
        q.append(paper)

    result = 1
    while q:
        x = q.popleft()
        # 더 높은 우선순위가 존재한다면

        #큐에 원소가 아직 존재할 때
        if q:
            # x보다 중요한 문서가 남아있다면
            if max(q) > x:
                q.append(x)
                if target_i == 0:
                    target_i = len(q) - 1
                else:
                    target_i -= 1
            #남아있는 원소 가운데 x보다 중요한 문서가 없으면 출력한다.
            else:
                # 출력한 문서가 target이면
                if target_i == 0:
                    answer.append(result)
                    break
                # target이 아니면
                else:
                    result += 1
                    if target_i == 0:
                        target_i = len(q) - 1
                    else:
                        target_i -= 1
        # 큐가 비어있다면
        if not q:
            answer.append(result)
            break

for a in answer:
    print(a)


# target_i 조정부분을 if (q) 맨 아래쪽으로 위치시켜도 됨
from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
answer = []
for _ in range(N):
    n, target_i = map(int, input().split())
    papers = list(map(int, input().split()))

    q = deque()

    for paper in papers:
        q.append(paper)

    result = 1
    while q:
        x = q.popleft()
        # 더 높은 우선순위가 존재한다면

        #큐에 원소가 아직 존재할 때
        if q:
            # x보다 중요한 문서가 남아있다면
            if max(q) > x:
                q.append(x)
            #남아있는 원소 가운데 x보다 중요한 문서가 없으면 출력한다.
            else:
                # 출력한 문서가 target이면
                if target_i == 0:
                    answer.append(result)
                    break
                # target이 아니면
                else:
                    result += 1
            # target_i를 조정해준다.
            if target_i == 0:
                target_i = len(q) - 1
            else:
                target_i -= 1

        # 큐가 비어있다면
        if not q:
            answer.append(result)
            break

for a in answer:
    print(a)