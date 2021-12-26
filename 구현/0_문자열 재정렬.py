"""
Facebook 인터뷰 문제

알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

[INPUT]
K1KA5CB7
[OUTPUT]
ABCKK13

[INPUT]
AJKDLSI412K4JSJ9D
[OUTPUT]
ADDIJJJKKLSS20
"""
import sys
input = lambda : sys.stdin.readline().rstrip()

s = list(input())
s.sort()
num = 0

for i in range(len(s)):
    if s[i].isdigit():
        num += int(s[i])
    else:
        break

print("".join(s[i:]) + str(num))