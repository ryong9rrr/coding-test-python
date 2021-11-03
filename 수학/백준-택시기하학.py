import sys
import math
input = sys.stdin.readline

r = int(input())

ud = format((r ** 2)*math.pi, ".6f")
md = (r ** 2)*2

print( ud )
print("%.6f" %md )