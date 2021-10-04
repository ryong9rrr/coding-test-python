import sys
input = sys.stdin.readline

word = input().rstrip()

for apb in range( ord('a'), ord('z') + 1 ) : # 97~122
    print(word.find(chr(apb)), end=" ") 