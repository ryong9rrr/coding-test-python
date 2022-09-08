N = int(input())
times = []
for _ in range(N):
    time = list(map(int, input().split()))
    times.append(time)

times.sort(key=lambda x:x[0])
times.sort(key=lambda x:x[1])
end = 0
cnt = 0
for a, b in times:
    if end <= a:
        end = b
        cnt += 1
print(cnt)