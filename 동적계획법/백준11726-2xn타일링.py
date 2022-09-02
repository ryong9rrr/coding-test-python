d = [0] * 1001
d[0], d[1], d[2] = 1, 1, 2
def dp(x:int):
    if x > 2:
        for i in range(3, x+1):
            d[i] = d[i-1] + d[i-2]

n = int(input())
dp(n)
print(d[n] % 10007)