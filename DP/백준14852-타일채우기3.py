d = [[0]*2 for _ in range(1000001)]
d[0][0] = 1
d[1][0] = 2
d[2][0] = 7
def dp(x):
    if x > 2:
        for i in range(3, x+1):
            d[i][1] = (d[i-3][0] + d[i-1][1]) % 1000000007
            d[i][0] = (2 * d[i-1][0] + 3 * d[i-2][0] + 2 * d[i][1]) % 1000000007

n = int(input())
dp(n)
print(d[n][0])