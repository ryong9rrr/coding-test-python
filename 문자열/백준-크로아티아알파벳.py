import sys
input = sys.stdin.readline

s = input().rstrip()

abp = ['dz=', 'c=', 's=', 'c-', 'd-', 'lj', 'nj', 'z=']

for i in abp :
    s = s.replace(i, '0')

print(len(s))
