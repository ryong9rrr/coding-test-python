d = [1, 1, 3]

def dp(x:int)->int:
    if x > 2:
        for i in range(3, x+1):
            result = (d[i-1] + 2*d[i-2]) % 10007
            d.append(result)
n = int(input())
dp(n)

print(d[n])