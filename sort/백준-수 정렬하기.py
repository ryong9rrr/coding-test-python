# O(n^2), selection-sort

import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    x = int(input())
    numbers.append(x)

def selection_sort(array:list, n:int):
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if array[min_index] >= array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

selection_sort(numbers, n)

for number in numbers:
    print(number)