from collections import defaultdict
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    
    visited = defaultdict(bool)

    def dfs(begin, target, words, count):
        print(begin)
        if begin == target:
            answer = count
            return
        
        for i, word in enumerate(words):
            if visited[word]:
                continue
            
            k = 0
            for j in range(len(begin)):
                if begin[j] == word[j]:
                    k += 1
            
            if k == (len(begin) - 1):
                visited[word] = True
                dfs(word, target, words, count + 1)
                visited[word] = False
    
    
    dfs(begin, target, words, 0)
    return answer