import sys
input = lambda: sys.stdin.readline().rstrip()

strings = input()
# 마지막 숫자까지 더해주기 위한 일종의 파싱
strings += "k"

result = 0
temp = ""
minus = False
for s in strings:
    if s == "+" or s == "-" or s == "k":
        if minus:
            result -= int(temp)
            temp = ""
        else:
            result += int(temp)
            temp = ""
    else:
        temp += s

    # minus가 나온 순간부터는 계속 -만 할 것이므로
    if not minus and s == "-":
        minus = True

print(result)