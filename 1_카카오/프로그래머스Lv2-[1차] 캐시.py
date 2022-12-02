from collections import deque

class LRU:
    HIT = 1
    MISS = 5
    
    def __init__(self, size):
        self.maxSize = size
        self.array = deque()
        self.time = 0
        
    def find(self, value):
        return value in self.array
    
    def remove(self, value):
        self.array.remove(value)
        
    def isMaxSize(self):
        return len(self.array) == self.maxSize
    
    def add(self, value):
        if self.find(value):
            self.remove(value)
            self.time += self.HIT
        else:
            self.time += self.MISS
        if self.isMaxSize():
            self.array.popleft()
        self.array.append(value)

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    cacheChangeAlgorithm = LRU(cacheSize)
    
    for city in cities:
        city = city.lower()
        cacheChangeAlgorithm.add(city)
    
    return cacheChangeAlgorithm.time
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.4MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.07ms, 10.1MB)
테스트 11 〉	통과 (103.21ms, 17.5MB)
테스트 12 〉	통과 (0.07ms, 10.4MB)
테스트 13 〉	통과 (0.22ms, 10MB)
테스트 14 〉	통과 (0.19ms, 10.2MB)
테스트 15 〉	통과 (0.26ms, 10.2MB)
테스트 16 〉	통과 (0.62ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.3MB)
테스트 18 〉	통과 (0.97ms, 10.3MB)
테스트 19 〉	통과 (0.88ms, 10.2MB)
테스트 20 〉	통과 (1.04ms, 10.3MB)
"""