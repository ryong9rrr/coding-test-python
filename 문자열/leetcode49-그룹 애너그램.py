# 80ms // 애너그램을 찾아내는 가장 좋은 방법은 정렬하는 것이다.
def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagrams = defaultdict(list)
    
    # sorted는 list를 리턴함(sort는 None을 리턴)
    for word in strs:
        anagrams["".join(sorted(word))].append(word)
        
    return list(anagrams.values())