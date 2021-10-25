import sys
input = lambda : sys.stdin.readline()

str = input()

result = 0
temp = "0"
minus = False
for s in list(str):
    if s == "+" or s == "-" or s == "\n":
        if minus:
            result -= int(temp)
            temp = "0"
        else:
            result += int(temp)
            temp = "0"
    else:
        temp += s

    if s == "-":
        minus = True
        continue

print(result)